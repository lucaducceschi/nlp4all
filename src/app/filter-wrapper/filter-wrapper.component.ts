import { preserveWhitespacesDefault } from '@angular/compiler';
import { INFERRED_TYPE } from '@angular/compiler/src/output/output_ast';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { AnyForUntypedForms, FormBuilder, Validators } from '@angular/forms';
import { filter } from 'lodash';
import { Subject } from 'rxjs';
import { aTokenLens, TokenLens } from '../models/document-token-lens';
import {
  aFilterCard,
  aSentenceCard,
  aSentenceRequest,
  aSequenceCard,
  aSequenceRequest,
  Card,
  FilterCard,
  initialCardPosition,
  SentenceCard,
  SequenceCard,
} from '../models/filter-card';
import { aLens, DISABLED_FILTER_LENS } from '../models/filter-lens';
import { aFilterRequest, UposValues } from '../models/filter-request';
import { FilterService } from '../services/filter.service';

@Component({
  selector: 'app-filter-wrapper',
  templateUrl: './filter-wrapper.component.html',
  styleUrls: ['./filter-wrapper.component.scss'],
})
export class FilterWrapperComponent {
  @Input() selectedDocId: string = '';
  @Input() selectedTabIndex: number;
  @Input() resetCards: Subject<any>;

  @Output() updateTokenLensesEvent = new EventEmitter();

  filterCards: FilterCard[] = [];
  sentenceCards: SentenceCard[] = [];
  sequenceCards: SequenceCard[] = [];

  tokenLenses: TokenLens[] = [];

  constructor(private filterService: FilterService, private fb: FormBuilder) {}

  ngOnInit() {
    this.resetCards.subscribe(() => {
      this.filterCards = [];
      this.sentenceCards = [];
      this.sequenceCards = [];
    });
  }

  addFilterCardToMainPanel($event: string) {
    if (this.selectedDocId != '') {
      if ($event == 'SENTENCE') {
        this.sentenceCards.push(
          aSentenceCard({
            id: Math.floor(Math.random() * 100000),
            position: initialCardPosition(),
            notApplied: true,
            active: false,
            zIndex:
              this.filterCards.length +
              this.sentenceCards.length +
              this.sequenceCards.length,
            sentenceRequest: aSentenceRequest({
              id_text: this.selectedDocId,
              s_types: [],
              word_ids: [],
            }),
            embeddingFor: undefined,
            lens: DISABLED_FILTER_LENS,
            sentenceFormGroup: this.fb.group({
              type: [undefined],
            }),
            lensFormGroup: this.fb.group({
              font: ['Arial'],
              color: ['#000000'],
              highlight: ['#FFFFFF'],
            }),
            lensFormSubscription: undefined,
          })
        );
      } else if ($event == 'SEQUENCE') {
        this.sequenceCards.push(
          aSequenceCard({
            id: Math.floor(Math.random() * 100000),
            zIndex:
              this.filterCards.length +
              this.sentenceCards.length +
              this.sequenceCards.length,
            sequenceRequest: aSequenceRequest({
              id_text: this.selectedDocId,
              after: [],
              before: [],
              distance: undefined,
            }),
            sequenceFor: [],
            sequenceFormGroup: this.fb.group({
              distance: [undefined],
            }),
            lines: [],
          })
        );
      } else {
        this.filterCards.push(
          aFilterCard({
            id: Math.floor(Math.random() * 100000),
            position: initialCardPosition(),
            notApplied: true,
            active: false,
            zIndex:
              this.filterCards.length +
              this.sentenceCards.length +
              this.sequenceCards.length,
            filterRequest: aFilterRequest({
              id_text: this.selectedDocId,
              upos: $event,
            }),
            lens: DISABLED_FILTER_LENS,
            filterFormGroup: this.fb.group({
              lemma: [undefined],
              fem: [false],
              masc: [false],
              sing: [false],
              plur: [false],
              tense: ['All'],
              ner: [undefined],
              verbform: ['All'],
              def: [false],
              ind: [false],
              numtype: ['All'],
              prontype: ['All'],
              polarity: ['All'],
              foreign: [false],
            }),
            lensFormGroup: this.fb.group({
              font: ['Arial'],
              color: ['#000000'],
              highlight: ['#FFFFFF'],
            }),
            lensFormSubscription: undefined,
          })
        );
      }
    }
  }

  applyFilter(filterCard: FilterCard) {
    this.filterService
      .getFilter(filterCard.filterRequest)
      .subscribe((tokens) => {
        const tokenResultsIndex = this.tokenLenses.findIndex(
          (tokenLens) => tokenLens.cardId == filterCard.id
        );

        if (tokenResultsIndex != -1) {
          this.tokenLenses[tokenResultsIndex].tokenResult = tokens.split(' ');
          this.updateTokenLensesEvent.emit(this.tokenLenses);
        } else {
          this.tokenLenses.push(
            aTokenLens({
              cardId: filterCard.id,
              tokenResult: tokens.split(' '),
              lens: filterCard.lens,
            })
          );
          this.updateTokenLensesEvent.emit(this.tokenLenses);
        }
      });
  }

  applySentence(sentenceCard: SentenceCard) {
    const embeddedTokenLens = this.tokenLenses.find((tokenLens) => {
      return tokenLens.cardId == sentenceCard.embeddingFor;
    });
    sentenceCard.sentenceRequest.word_ids =
      embeddedTokenLens?.tokenResult || [];
    this.filterService
      .getSentence(sentenceCard.sentenceRequest)
      .subscribe((tokens) => {
        const tokenResultsIndex = this.tokenLenses.findIndex(
          (tokenLens) => tokenLens.cardId == sentenceCard.id
        );

        if (tokenResultsIndex != -1) {
          this.tokenLenses[tokenResultsIndex].tokenResult = tokens.split(' ');
          this.updateTokenLensesEvent.emit(this.tokenLenses);
        } else {
          this.tokenLenses.push(
            aTokenLens({
              cardId: sentenceCard.id,
              tokenResult: tokens.split(' '),
              lens: sentenceCard.lens,
            })
          );
          this.updateTokenLensesEvent.emit(this.tokenLenses);
        }
      });
  }

  applySequence($event: any) {
    const beforeTokenLens = this.tokenLenses.find(
      (tokenLens) => tokenLens.cardId == $event.sequenceCard.sequenceFor[0]
    );
    const afterTokenLens = this.tokenLenses.find(
      (tokenLens) => tokenLens.cardId == $event.sequenceCard.sequenceFor[1]
    );

    $event.sequenceCard.sequenceRequest.before =
      beforeTokenLens?.tokenResult || [];

    $event.sequenceCard.sequenceRequest.after =
      afterTokenLens?.tokenResult || [];

    this.filterService
      .getSequence($event.sequenceCard.sequenceRequest)
      .subscribe((sequenceResponse) => {
        const beforeTokenResults = Object.values(sequenceResponse).flatMap(
          (sequenceTokensBySentence) =>
            sequenceTokensBySentence.flatMap(([_, before]) => before)
        );

        const afterTokenResults = Object.values(sequenceResponse).flatMap(
          (sequenceTokensBySentence) =>
            sequenceTokensBySentence.flatMap(([after, _]) => after)
        );

        const beforeTokenLensIndex = this.tokenLenses.findIndex(
          (tokenLens) => tokenLens.cardId == $event.sequenceCard.sequenceFor[0]
        );
        const afterTokenLensIndex = this.tokenLenses.findIndex(
          (tokenLens) => tokenLens.cardId == $event.sequenceCard.sequenceFor[1]
        );

        this.tokenLenses[beforeTokenLensIndex].tokenResult = beforeTokenResults;
        this.tokenLenses[afterTokenLensIndex].tokenResult = afterTokenResults;

        this.updateTokenLensesEvent.emit(this.tokenLenses);
      });
  }

  applyLens(card: Card) {
    const tokenLensIndexToApplyLens = this.tokenLenses.findIndex(
      (tokenLens) => tokenLens.cardId == card.id
    );

    this.tokenLenses[tokenLensIndexToApplyLens].lens = card.lens;

    this.updateTokenLensesEvent.emit(this.tokenLenses);
  }

  removeFilterCard(filterCardToRemove: FilterCard) {
    const embeddingSentenceCardIndex = this.sentenceCards.findIndex(
      (sentenceCard) => sentenceCard.embeddingFor == filterCardToRemove.id
    );

    if (embeddingSentenceCardIndex != -1) {
      this.sentenceCards[embeddingSentenceCardIndex].line.remove();
      this.sentenceCards[embeddingSentenceCardIndex].line = undefined;
      this.sentenceCards[embeddingSentenceCardIndex].embeddingFor = undefined;
      this.sentenceCards[embeddingSentenceCardIndex].active = false;
      this.sentenceCards[embeddingSentenceCardIndex].lens =
        DISABLED_FILTER_LENS;

      const embeddingTokenLensIndex = this.tokenLenses.findIndex(
        (tokenLens) =>
          tokenLens.cardId == this.sentenceCards[embeddingSentenceCardIndex].id
      );

      if (embeddingTokenLensIndex != -1) {
        this.tokenLenses[embeddingTokenLensIndex].lens = DISABLED_FILTER_LENS;
        this.updateTokenLensesEvent.emit(this.tokenLenses);
      }
    }

    this.filterCards = this.filterCards.filter(
      (filterCard) => filterCard.id != filterCardToRemove.id
    );

    this.tokenLenses = this.tokenLenses.filter(
      (tokenLens) => tokenLens.cardId != filterCardToRemove.id
    );

    this.updateTokenLensesEvent.emit(this.tokenLenses);
  }

  removeSentenceCard(sentenceCardToRemove: SentenceCard) {
    const embeddingFilterCardIndex = this.filterCards.findIndex(
      (filterCard) => filterCard.id == sentenceCardToRemove.embeddingFor
    );

    if (embeddingFilterCardIndex != -1) {
      sentenceCardToRemove.line.remove();
      this.filterCards[embeddingFilterCardIndex].line = undefined;
    }

    this.sentenceCards = this.sentenceCards.filter(
      (sentenceCard) => sentenceCard.id != sentenceCardToRemove.id
    );

    this.tokenLenses = this.tokenLenses.filter(
      (tokenLens) => tokenLens.cardId != sentenceCardToRemove.id
    );

    this.updateTokenLensesEvent.emit(this.tokenLenses);
  }

  removeSequenceCard(sequenceCardToRemove: SequenceCard) {
    sequenceCardToRemove.lines.forEach((line) => line.remove());

    const sequenceFilterCardBeforeIndex = this.filterCards.findIndex(
      (filterCard) => filterCard.id == sequenceCardToRemove.sequenceFor[0]
    );

    if (sequenceFilterCardBeforeIndex != -1) {
      this.filterCards[sequenceFilterCardBeforeIndex].line = undefined;
    }

    const sequenceFilterCardAfterIndex = this.filterCards.findIndex(
      (filterCard) => filterCard.id == sequenceCardToRemove.sequenceFor[0]
    );

    if (sequenceFilterCardAfterIndex != -1) {
      this.filterCards[sequenceFilterCardAfterIndex].line = undefined;
    }

    this.sequenceCards = this.sequenceCards.filter(
      (sequenceCard) => sequenceCard.id != sequenceCardToRemove.id
    );

    this.tokenLenses = this.tokenLenses.filter(
      (tokenLens) => tokenLens.cardId != sequenceCardToRemove.id
    );

    this.updateTokenLensesEvent.emit(this.tokenLenses);
  }
}
