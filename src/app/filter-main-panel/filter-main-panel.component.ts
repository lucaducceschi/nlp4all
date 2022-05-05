import {
  AfterViewInit,
  Component,
  ElementRef,
  EventEmitter,
  Input,
  OnInit,
  Output,
  SimpleChanges,
} from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { MatExpansionPanelHeader } from '@angular/material/expansion';
import {
  MatSlideToggle,
  MatSlideToggleChange,
} from '@angular/material/slide-toggle';
import { take } from 'rxjs';
import { first, SequenceError, single, Subject, Subscription, tap } from 'rxjs';
import {
  aCardPosition,
  Card,
  FilterCard,
  initialCardPosition,
  SentenceCard,
  SequenceCard,
} from '../models/filter-card';
import { DISABLED_FILTER_LENS } from '../models/filter-lens';
import {
  DefiniteValues,
  ForeignValues,
  GenderValues,
  NumberValues,
  NumTypeValues,
  PolarityValues,
  ProntypeValues,
  TenseValues,
  VerbFormValues,
} from '../models/filter-request';
import { RemoveCardsDialogComponent } from '../remove-cards-dialog/remove-cards-dialog.component';

declare var LeaderLine: any;

@Component({
  selector: 'app-filter-main-panel',
  templateUrl: './filter-main-panel.component.html',
  styleUrls: ['./filter-main-panel.component.scss'],
})
export class FilterMainPanelComponent {
  @Input() filterCards: FilterCard[] = [];
  @Input() sentenceCards: SentenceCard[] = [];
  @Input() sequenceCards: SequenceCard[] = [];

  @Input() selectedTabIndex: number;

  @Output() applyFilterEvent = new EventEmitter();
  @Output() applySentenceEvent = new EventEmitter();
  @Output() applySequenceEvent = new EventEmitter();

  @Output() applyLensEvent = new EventEmitter();

  @Output() removeFilterCardEvent = new EventEmitter();
  @Output() removeSentenceCardEvent = new EventEmitter();
  @Output() removeSequenceCardEvent = new EventEmitter();

  zIndexMax: number;

  linkEvent = new Subject<string>();
  linkMode = false;

  constructor(private elementRef: ElementRef, public dialog: MatDialog) {}

  ngOnChanges() {
    if (this.selectedTabIndex != 1) {
      this.sentenceCards.forEach((sentenceCard) => {
        if (sentenceCard.line) {
          sentenceCard.line.hide('none');
        }
      });

      this.sequenceCards.forEach((sequenceCard) => {
        if (sequenceCard.lines.length > 0) {
          sequenceCard.lines.forEach((line) => line.hide('none'));
        }
      });
    }
  }

  ngAfterContentChecked() {
    if (this.isFilterMainPanelVisible()) {
      if (this.selectedTabIndex == 1) {
        this.sentenceCards.forEach((sentenceCard) => {
          if (sentenceCard.line) {
            sentenceCard.line.show('none');
            sentenceCard.line.position();
          }
        });
        this.sequenceCards.forEach((sequenceCard) => {
          if (sequenceCard.lines.length > 0) {
            sequenceCard.lines.forEach((line) => {
              line.show('none');
              line.position();
            });
          }
        });
      }

      this.zIndexMax = this.filterCards
        .map((card) => card.zIndex)
        .reduce((prev, curr) => Math.max(prev, curr), 0);
    }
  }

  //risoluzione bug della card che si aggiunge nel primo posto libero
  getFreePosition(card: Card) {
    if (card.position.x == 0 && card.position.y == 0) {
      const boundaryHeight = document.querySelector('.boundary').clientHeight;
      const boundaryWidth = document.querySelector('.boundary').clientWidth;

      let newX = Math.floor(Math.random() * (boundaryWidth - 310));
      let newY = Math.floor(Math.random() * (boundaryHeight - 50));

      const allX = this.filterCards.map((filterCard) => filterCard.position.x);
      const allY = this.filterCards.map((filterCard) => filterCard.position.y);

      while (
        (allX.includes(newX) && allY.includes(newY)) ||
        (allX.some((x) => newX > x && newX < x + 310) &&
          allY.some((y) => newY > y && newY < y + 50))
      ) {
        newX = Math.floor(Math.random() * (boundaryWidth - 310));
        newY = Math.floor(Math.random() * (boundaryHeight - 50));
      }
      const position = aCardPosition({
        x: newX,
        y: newY,
      });
      card.position = position;
      return position;
    } else {
      return card.position;
    }
  }

  moveUp(card: FilterCard | SentenceCard | SequenceCard) {
    if (card.zIndex < this.zIndexMax) {
      card.zIndex = this.zIndexMax + 1;
    }
  }

  expandFilterCard(panelH: MatExpansionPanelHeader) {
    panelH._toggle();
  }

  isFilterMainPanelVisible(): boolean {
    return this.elementRef.nativeElement.offsetParent != null;
  }

  linkWithFilterCard(panelH: MatExpansionPanelHeader, card: FilterCard) {
    if (card.line) {
      card.line.position();
    }
    if (this.linkMode) {
      panelH._toggle();
      this.linkEvent.next(card.id.toString());
    }
  }

  linkFilterCard($event: any, card: SentenceCard) {
    $event.stopPropagation();
    const startElement = document.getElementById(card.id.toString());
    if (card.line == undefined) {
      this.linkMode = true;
      this.linkEvent
        .pipe(
          first(),
          tap((endElementId) => {
            const endElement = document.getElementById(endElementId);
            let line = new LeaderLine(startElement, endElement);
            line.setOptions({
              endPlug: 'behind',
            });
            card.line = line;
            const endElementIndex = this.filterCards.findIndex(
              (filterCard) => filterCard.id == parseInt(endElementId)
            );
            this.filterCards[endElementIndex].line = line;
            card.embeddingFor = parseInt(endElementId);
            this.linkMode = false;
          })
        )
        .subscribe();
    }
  }

  unlinkFilterCard(
    $event: any,
    card: SentenceCard,
    slideToggle: MatSlideToggle
  ) {
    $event.stopPropagation();
    card.line.remove();
    card.line = undefined;
    const endElementIndex = this.filterCards.findIndex(
      (filterCard) => filterCard.id == card.embeddingFor
    );
    this.filterCards[endElementIndex].line = undefined;
    if (slideToggle.checked) {
      slideToggle.toggle();
      slideToggle.change.emit({
        source: slideToggle,
        checked: false,
      });
    }
    card.embeddingFor = undefined;
  }

  linkSequenceFilterCard($event: any, card: SequenceCard) {
    $event.stopPropagation();
    const startElement = document.getElementById(card.id.toString());
    if (card.lines.length < 2) {
      this.linkMode = true;
      this.linkEvent
        .pipe(
          take(2),
          tap((endElementId) => {
            const endElement = document.getElementById(endElementId);
            let line = new LeaderLine(startElement, endElement);
            line.setOptions({
              endPlug: 'behind',
            });
            card.lines.push(line);
            const endElementIndex = this.filterCards.findIndex(
              (filterCard) => filterCard.id == parseInt(endElementId)
            );
            this.filterCards[endElementIndex].line = line;
            console.log(card.sequenceFor);
            card.sequenceFor.push(parseInt(endElementId));
            if (card.sequenceFor.length == 2) {
              this.linkMode = false;
            }
          })
        )
        .subscribe();
    }
  }

  unlinkSequenceFilterCard($event: any, card: SequenceCard) {
    $event.stopPropagation();
    card.lines.forEach((line) => line.remove());
    card.lines = [];
    const beforeEndElementIndex = this.filterCards.findIndex(
      (filterCard) => filterCard.id == card.sequenceFor[0]
    );
    const afterEndElementIndex = this.filterCards.findIndex(
      (filterCard) => filterCard.id == card.sequenceFor[1]
    );
    this.filterCards[beforeEndElementIndex].line = undefined;
    this.filterCards[afterEndElementIndex].line = undefined;
    card.sequenceFor = [];
  }

  updateLine(card: FilterCard | SentenceCard | SequenceCard) {
    if (this.isSequenceCard(card)) {
      card.lines.forEach((line) => line.position());
    } else {
      if (card.line) card.line.position();
    }
  }

  isSequenceCard(
    card: FilterCard | SentenceCard | SequenceCard
  ): card is SequenceCard {
    return (<SequenceCard>card).lines !== undefined;
  }

  updateLineAfterMove(card: FilterCard | SentenceCard | SequenceCard) {
    if (this.isSequenceCard(card)) {
      card.lines.forEach((line) => line.position());
    } else {
      if (card.line) card.line.position();
    }
  }

  //REMOVE
  removeFilterCard(filterCard: FilterCard) {
    const dialogRef = this.dialog.open(RemoveCardsDialogComponent);
    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.removeFilterCardEvent.emit(filterCard);
      }
    });
  }

  removeSentenceCard(sentenceCard: SentenceCard) {
    const dialogRef = this.dialog.open(RemoveCardsDialogComponent);
    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.removeSentenceCardEvent.emit(sentenceCard);
      }
    });
  }

  removeSequenceCard(sequenceCard: SequenceCard) {
    const dialogRef = this.dialog.open(RemoveCardsDialogComponent);
    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.removeSequenceCardEvent.emit(sequenceCard);
      }
    });
  }

  //TOGGLE
  toggleFilterLens($event: MatSlideToggleChange, filterCard: FilterCard) {
    if ($event.checked) {
      filterCard.active = true;
      this.applyLens(filterCard);
      filterCard.lensFormSubscription =
        filterCard.lensFormGroup.valueChanges.subscribe(() =>
          this.applyLens(filterCard)
        );
    } else {
      filterCard.active = false;
      this.disableLens(filterCard);
      filterCard.lensFormSubscription.unsubscribe();
    }
  }

  toggleSentenceLens($event: MatSlideToggleChange, sentenceCard: SentenceCard) {
    if ($event.checked) {
      sentenceCard.active = true;
      this.applyLens(sentenceCard);

      sentenceCard.lensFormSubscription =
        sentenceCard.lensFormGroup.valueChanges.subscribe(() =>
          this.applyLens(sentenceCard)
        );
    } else {
      sentenceCard.active = false;
      this.disableLens(sentenceCard);
      sentenceCard.lensFormSubscription.unsubscribe();
    }
  }

  //LENS
  applyLens(card: Card) {
    card.lens = {
      ...card.lens,
      font: card.lensFormGroup.value.font,
      color: card.lensFormGroup.value.color,
      highlight: card.lensFormGroup.value.highlight,
    };

    this.applyLensEvent.emit(card);
  }

  disableLens(card: Card) {
    card.lens = DISABLED_FILTER_LENS;
    this.applyLensEvent.emit(card);
  }

  //APPLY
  applyFilter(filterCard: FilterCard) {
    filterCard.filterRequest = {
      ...filterCard.filterRequest,
      lemma: filterCard.filterFormGroup.value.lemma,
      number: this.getNumberValue(filterCard.filterFormGroup.value),
      gender: this.getGenderValue(filterCard.filterFormGroup.value),
      tense: this.getTenseValue(filterCard.filterFormGroup.value),
      verbform: this.getVerbFormValue(filterCard.filterFormGroup.value),
      definite: this.getDefiniteValue(filterCard.filterFormGroup.value),
      numtype: this.getNumtypeValue(filterCard.filterFormGroup.value),
      prontype: this.getProntypeValue(filterCard.filterFormGroup.value),
      polarity: this.getPolarityValue(filterCard.filterFormGroup.value),
      foreign: this.getForeignValue(filterCard.filterFormGroup.value),
    };

    filterCard.notApplied = false;

    this.applyFilterEvent.emit(filterCard);
  }

  applySentence(sentenceCard: SentenceCard) {
    sentenceCard.sentenceRequest = {
      ...sentenceCard.sentenceRequest,
      s_types: [sentenceCard.sentenceFormGroup.value.type],
    };

    sentenceCard.notApplied = false;

    const embeddedFilterCard = this.filterCards.find(
      (filterCard) => filterCard.id == sentenceCard.embeddingFor
    );

    if (!embeddedFilterCard.active) {
      const filterCardDisabledLens = {
        ...embeddedFilterCard,
        filterLens: DISABLED_FILTER_LENS,
      };

      this.applyFilterEvent.emit(filterCardDisabledLens);
      setTimeout(() => this.applySentenceEvent.emit(sentenceCard), 1000);
    } else {
      this.applySentenceEvent.emit(sentenceCard);
    }
  }

  applySequence(sequenceCard: SequenceCard) {
    sequenceCard.sequenceRequest = {
      ...sequenceCard.sequenceRequest,
      distance: parseInt(sequenceCard.sequenceFormGroup.value.distance),
    };

    const filterCardBeforeWithDisabledLens = {
      ...this.filterCards.find(
        (filterCard) => filterCard.id == sequenceCard.sequenceFor[1]
      ),
      filterLens: DISABLED_FILTER_LENS,
    };

    const filterCardAfterWithDisabledLens = {
      ...this.filterCards.find(
        (filterCard) => filterCard.id == sequenceCard.sequenceFor[0]
      ),
      filterLens: DISABLED_FILTER_LENS,
    };

    this.applyFilterEvent.emit(filterCardBeforeWithDisabledLens);

    setTimeout(
      () => this.applyFilterEvent.emit(filterCardAfterWithDisabledLens),
      1000
    );

    setTimeout(
      () =>
        this.applySequenceEvent.emit({
          sequenceCard: sequenceCard,
          beforeCard: filterCardBeforeWithDisabledLens,
          afterCard: filterCardAfterWithDisabledLens,
        }),
      2000
    );
  }

  getNumberValue(value: any) {
    if (value.sing && !value.plur) {
      return NumberValues.SING;
    } else if (value.plur && !value.sing) {
      return NumberValues.PLUR;
    } else {
      return undefined;
    }
  }

  getGenderValue(value: any) {
    if (value.masc && !value.fem) {
      return GenderValues.MASC;
    } else if (value.fem && !value.masc) {
      return GenderValues.FEM;
    } else {
      return undefined;
    }
  }

  getDefiniteValue(value: any) {
    if (value.def && !value.ind) {
      return DefiniteValues.DEF;
    } else if (value.ind && !value.def) {
      return DefiniteValues.IND;
    } else {
      return undefined;
    }
  }

  getTenseValue(value: any) {
    switch (value.tense) {
      case TenseValues.FUT:
        return TenseValues.FUT;
      case TenseValues.IMP:
        return TenseValues.IMP;
      case TenseValues.PAST:
        return TenseValues.PAST;
      case TenseValues.PRES:
        return TenseValues.PRES;
      default:
        return null;
    }
  }

  getVerbFormValue(value: any) {
    switch (value.tense) {
      case VerbFormValues.FIN:
        return VerbFormValues.FIN;
      case VerbFormValues.GER:
        return VerbFormValues.GER;
      case VerbFormValues.INF:
        return VerbFormValues.INF;
      case VerbFormValues.PART:
        return VerbFormValues.PART;
      default:
        return null;
    }
  }

  getNumtypeValue(value: any) {
    switch (value.numtype) {
      case NumTypeValues.CARD:
        return NumTypeValues.CARD;
      case NumTypeValues.ORD:
        return NumTypeValues.ORD;
      default:
        return null;
    }
  }

  getPolarityValue(value: any) {
    switch (value.numtype) {
      case PolarityValues.NEG:
        return PolarityValues.NEG;
      case PolarityValues.POS:
        return PolarityValues.POS;
      default:
        return null;
    }
  }

  getProntypeValue(value: any) {
    switch (value.prontype) {
      case ProntypeValues.ART:
        return ProntypeValues.ART;
      case ProntypeValues.DEM:
        return ProntypeValues.DEM;
      case ProntypeValues.EXC:
        return ProntypeValues.EXC;
      case ProntypeValues.IND:
        return ProntypeValues.IND;
      case ProntypeValues.INT:
        return ProntypeValues.INT;
      case ProntypeValues.NEG:
        return ProntypeValues.NEG;
      case ProntypeValues.PRS:
        return ProntypeValues.PRS;
      case ProntypeValues.REL:
        return ProntypeValues.REL;
      case ProntypeValues.TOT:
        return ProntypeValues.TOT;
      default:
        return null;
    }
  }

  getForeignValue(value: any) {
    if (value.foreign) {
      return ForeignValues.YES;
    } else {
      return null;
    }
  }
}
