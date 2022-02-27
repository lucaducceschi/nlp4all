import { Component, OnInit } from '@angular/core';
import { fakeDocument } from '../models/fake-document';
import { aDocument, Document } from '../models/document';

@Component({
  selector: 'app-panel-wrapper',
  templateUrl: './panel-wrapper.component.html',
  styleUrls: ['./panel-wrapper.component.scss'],
})
export class PanelWrapperComponent {
  documentList: Document[] = [
    aDocument({
      docId: '1',
      title: 'Moby dick',
      author: 'Pia',
      language: 'Brindisino',
    }),
  ]; //TRAMITE DIALOG CHIAMATA AL SERVER listDocuments ->
  selectedDocument: string = '';

  constructor() {}

  changeSelectedDocument($event: Document) {
    this.selectedDocument = fakeDocument; //CHIAMATA AL SERVER getDocumentById(docId)
  }

  removeDocumentFromList($event: string) {
    this.documentList = this.documentList.filter(
      (document) => document.docId != $event
    );
  }
}
