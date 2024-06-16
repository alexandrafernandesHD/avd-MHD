import spacy 
from jjcli import *
from collections import Counter


cl = clfilter("")
all_propn_words = Counter()
for linha in cl.input():
    palavras = linha.split()
    if len(palavras) >= 3:
        if palavras[2] == "PROPN":
            lema = palavras[1]
            all_propn_words.update([palavras[1]])


output = open("propn.csv", "w", encoding="UTF-8")
for propn, oco in sorted(all_propn_words.items(), key=lambda x: x[1], reverse=True):
    print(f"{propn}, {oco}", file = output)

