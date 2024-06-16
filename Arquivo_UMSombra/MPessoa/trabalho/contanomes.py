import spacy 
from jjcli import *
from collections import Counter

cl = clfilter("")
all_nomes = Counter()
for linha in cl.input():
    palavras = linha.split()
    if len(palavras) >= 3:
        if palavras[2] == "NOUN":
            lema = palavras[1]
            all_nomes.update([palavras[1]]) 

output = open("nomes.csv", "w", encoding="UTF-8")
for nome, oco in sorted(all_nomes.items(), key=lambda x: x[1], reverse=True):
    print(f"{nome}, {oco}", file = output)


