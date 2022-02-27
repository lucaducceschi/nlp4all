import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Document } from '../models/document';

@Component({
  selector: 'app-side-panel',
  templateUrl: './side-panel.component.html',
  styleUrls: ['./side-panel.component.scss'],
})
export class SidePanelComponent {
  @Input() documentList: Document[] = [];
  @Output() documentListSelectionChangeEvent = new EventEmitter<any>();
  @Output() removeDocumentFromListEvent = new EventEmitter<any>();

  constructor() {}

  documentListSelectionChange($event: any) {
    this.documentListSelectionChangeEvent.emit($event);
  }

  removeDocumentFromList($event: any) {
    this.removeDocumentFromListEvent.emit($event);
  }
}
