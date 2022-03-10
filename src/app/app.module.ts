import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { WrapperComponent } from './wrapper/wrapper.component';
import { HeaderComponent } from './header/header.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { SidePanelComponent } from './side-panel/side-panel.component';
import { MainPanelComponent } from './main-panel/main-panel.component';
import { PanelWrapperComponent } from './panel-wrapper/panel-wrapper.component';
import { DocumentComponent } from './document/document.component';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { SidePanelDocumentListComponent } from './side-panel-document-list/side-panel-document-list.component';
import { HttpClientModule } from '@angular/common/http';
import { MatDialogModule } from '@angular/material/dialog';
import { AddTextsDialogComponent } from './add-texts-dialog/add-texts-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    WrapperComponent,
    HeaderComponent,
    SidePanelComponent,
    MainPanelComponent,
    PanelWrapperComponent,
    DocumentComponent,
    SidePanelDocumentListComponent,
    AddTextsDialogComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatToolbarModule,
    MatCardModule,
    MatListModule,
    MatButtonModule,
    MatIconModule,
    MatDialogModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
