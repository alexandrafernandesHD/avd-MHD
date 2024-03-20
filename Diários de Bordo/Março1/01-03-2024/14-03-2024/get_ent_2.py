# pip install -U spacy
# python -m spacy download pt_core_news_lg
# en_core_web_sm
import spacy
from jjcli import *

def main():
    cl = clfilter()
    for text in cl.text():
        proctexto(text)

def proctexto(text):
    nlp = spacy.load("pt_core_news_lg")
    doc = nlp(text)
    for entity in doc.ents:
        print(entity.text, entity.label_)

main()
