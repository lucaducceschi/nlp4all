import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-main-panel',
  templateUrl: './main-panel.component.html',
  styleUrls: ['./main-panel.component.scss'],
})
export class MainPanelComponent {
  @Input() selectedDocument: string = '';

  constructor() {}
}
