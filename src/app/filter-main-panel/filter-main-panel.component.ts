import { Component, Input, OnInit } from '@angular/core';
import { FilterCard } from '../filter-wrapper/filter-wrapper.component';

@Component({
  selector: 'app-filter-main-panel',
  templateUrl: './filter-main-panel.component.html',
  styleUrls: ['./filter-main-panel.component.scss'],
})
export class FilterMainPanelComponent implements OnInit {
  @Input() filterCards: FilterCard[] = [];

  constructor() {}

  ngOnInit(): void {}
}
