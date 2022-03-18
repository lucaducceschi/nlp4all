import { Component, OnInit } from '@angular/core';
import {
  aFilterRequest,
  FilterRequest,
  UposValues,
} from '../models/filter-request';
import { FilterService } from '../services/filter.service';

@Component({
  selector: 'app-filter-wrapper',
  templateUrl: './filter-wrapper.component.html',
  styleUrls: ['./filter-wrapper.component.scss'],
})
export class FilterWrapperComponent implements OnInit {
  filterCards: FilterCard[] = [];
  constructor(private filterService: FilterService) {}

  ngOnInit(): void {}

  addFilterCardToMainPanel() {
    const filterCard = aFilterCard({
      id: Math.floor(Math.random() * 100),
      filterRequest: aFilterRequest({
        id_text: 'short_sample',
        upos: UposValues.ADJ,
      }),
    });
    this.filterCards.push(filterCard);

    this.filterService
      .getFilter(filterCard.filterRequest)
      .subscribe((data) => console.log(data));
  }
}

export interface FilterCard {
  id: number;
  filterRequest: FilterRequest;
}

export function aFilterCard(filterCard: FilterCard) {
  return filterCard;
}
