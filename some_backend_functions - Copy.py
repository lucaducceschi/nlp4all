# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:16:22 2020

@author: luca
"""
import stanza
import requests
import re

nlp_it = stanza.Pipeline("it", processors="tokenize, pos, lemma", verbose = False ) #  , use_gpu=True 
sample_it_url = "https://www.gutenberg.org/cache/epub/18456/pg18456.txt" # Pirandello, Enrico 4

# this is to get a sample text from gutenberg

def clean_text_from_gutenberg(a_url):
  r  = requests.get(a_url)
  r.encoding = "utf-8-sig"
  t = r.text
  t = re.sub("\r", "\n", t)
  t = re.sub(r"\n+", r"\n",t)
  start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK.* \*\*\*", t).span()[1]
  end = re.search("End of the Project Gutenberg EBook of", t).span()[0]
  return t[start:end] 



def generate_html(doc_):

    # this is to obtain the html
#### TODO: eliminate &nbsp at the beginning of the sentence 
    new_txt=""
    nsent=1
    
    for sent in doc_.sentences:
      new_txt+="<span class='sentence' id='sent_" + str(nsent) +"'>"
      new_sent=""
      for tok in sent.words:
        if tok.pos != "PUNCT":
          new_sent+=f"<span>&nbsp</span><span class='word' id='{tok.id}'>{tok.text}</span>"
        else:
          new_sent+=f"<span class='word' id='{tok.id}'>{tok.text}</span>"

      new_txt+= new_sent + "</span><span><br></span>" + "\n"
      nsent+=1
    return(new_txt)

def generate_json(doc_):
  # returns the dictioanry that contains sentences and ids
  c = 1
  d = {}
  for sent in doc_.sentences:
    d["sent_"+str(c)] = sent.to_dict()
    c += 1
  return d



class verbfilter

# raw_pirandello = clean_text_from_gutenberg(sample_it_url).strip()
# # processed_pirandello = nlp_it(raw_pirandello)


# small_raw = re.sub(r"([A-zè,])\n([,èA-z])",r"\1 \2", raw_pirandello[423:50000])
# small_raw = re.sub(r"_[ \.\(\)\,\!;:A-zòàìùéè]+\._", "",small_raw)
# small_doc = nlp_it(small_raw)