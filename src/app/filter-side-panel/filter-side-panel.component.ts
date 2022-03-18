import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-filter-side-panel',
  templateUrl: './filter-side-panel.component.html',
  styleUrls: ['./filter-side-panel.component.scss'],
})
export class FilterSidePanelComponent implements OnInit {
  @Output() addFilterCardEvent = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  addFilterCard() {
    this.addFilterCardEvent.emit();
  }
}
