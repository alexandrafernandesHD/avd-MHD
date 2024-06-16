import spacy 
from jjcli import *
from collections import Counter

cl = clfilter("")
all_adjetivos = Counter()
for linha in cl.input():
    palavras = linha.split()
    if len(palavras) >= 3:
        if palavras[2] == "ADJ":
            lema = palavras[1]
            all_adjetivos.update([palavras[1]]) 

output = open("adjetivos.csv", "w", encoding="UTF-8")
for adj, oco in sorted(all_adjetivos.items(), key=lambda x: x[1], reverse=True):
    print(f"{adj}, {oco}", file = output)


