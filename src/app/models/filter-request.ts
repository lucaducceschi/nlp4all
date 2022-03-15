export interface FilterRequest {
  id_text: string;
  upos: string;
  lemma: string;
  gender: string;
  number: string;
}

export function aFilterRequest(filterRequest: FilterRequest) {
  return filterRequest;
}
