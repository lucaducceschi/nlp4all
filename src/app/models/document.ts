export interface Document {
  docId: string;
  title: string;
  author: string;
  language: string;
}

export function aDocument(document: Document) {
  return document;
}
