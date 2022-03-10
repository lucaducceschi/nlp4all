import { Component, OnInit } from '@angular/core';
import { fakeDocument } from '../models/fake-document';
import { aDocument, Document } from '../models/document';
import { DocumentService } from '../services/document.service';

@Component({
  selector: 'app-panel-wrapper',
  templateUrl: './panel-wrapper.component.html',
  styleUrls: ['./panel-wrapper.component.scss'],
})
export class PanelWrapperComponent {
  documentList: Document[] = [];
  selectedDocument: string = '';
  selectedDocId: string = '';

  constructor(private documentService: DocumentService) {}

  changeSelectedDocument($event: Document) {
    this.documentService.getDocument($event.docId).subscribe((data) => {
      this.selectedDocument = data;
      this.selectedDocId = $event.docId;
    });
  }

  removeDocumentFromList($event: string) {
    if (this.selectedDocId == $event) {
      this.selectedDocument = '';
    }
  }
}
