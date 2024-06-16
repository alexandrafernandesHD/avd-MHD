import spacy
from jjcli import *
from collections import Counter

# Carregar o modelo de linguagem do spaCy
nlp = spacy.load("pt_core_news_sm")

cl = clfilter("")
all_verbs = Counter()

# Obter a lista de stop words do spaCy
stopwords = set(nlp.Defaults.stop_words)
stopverbs = set()

# Processar cada stop word para verificar se é um verbo
for word in stopwords:
    doc = nlp(word)
    if doc and doc[0].pos_ == "VERB":
        stopverbs.add(word)

for linha in cl.input():
    palavras = linha.split()
    if len(palavras) >= 3:
        if palavras[2] == "VERB":
            lema = palavras[1]
            if lema[-1] != "r":
                continue
            if lema in stopverbs:
                continue
            all_verbs.update([lema]) 

output = open("verbos.csv", "w", encoding="UTF-8")
for verbo, oco in sorted(all_verbs.items(), key=lambda x: x[1], reverse=True):
    print(f"{verbo}, {oco}", file=output)
