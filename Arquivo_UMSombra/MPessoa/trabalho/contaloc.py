import spacy 
from jjcli import *
from collections import Counter

# Configurar o filtro de linha de comando
cl = clfilter("")
all_loc_words = Counter()

# Iterar sobre cada linha do input
for linha in cl.input():
    if "LOC" in linha:
        # Dividir a linha no primeiro TAB e pegar a primeira parte
        primeira_parte = linha.split('\t')[0]
        # Atualizar o contador com a primeira parte da linha
        all_loc_words.update([primeira_parte])


output = open("loc.csv", "w", encoding="UTF-8")

# Escrever os resultados no arquivo, ordenados por frequência
for loc, oco in sorted(all_loc_words.items(), key=lambda x: x[1], reverse=True):
    print(f"{loc}, {oco}", file = output)



