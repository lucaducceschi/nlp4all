import { Component } from '@angular/core';
import { TokenLens } from '../models/document-token-lens';

@Component({
  selector: 'app-wrapper',
  templateUrl: './wrapper.component.html',
  styleUrls: ['./wrapper.component.scss'],
})
export class WrapperComponent {
  selectedDocId: string = '';
  selectedTabIndex: number;

  tokenLenses: TokenLens[] = [];

  updateSelectedDocId($event: any) {
    this.selectedDocId = $event;
  }

  updateTokenLenses(tokenLenses: TokenLens[]) {
    this.tokenLenses = [...tokenLenses];
  }

  updateSelectedTabIndex($event: number) {
    this.selectedTabIndex = $event;
  }
}
