import spacy
from jjcli import *
from collections import Counter

# Configurar o filtro de linha de comando
cl = clfilter("")
all_per_words = Counter()

# Iterar sobre cada linha do input
for linha in cl.input():
    if "PER" in linha:
        # Dividir a linha no primeiro TAB e pegar a primeira parte
        primeira_parte = linha.split('\t')[0]
        # Atualizar o contador com a primeira parte da linha
        all_per_words.update([primeira_parte])

# Abrir o arquivo de saída para escrever os resultados
output = open("per.csv", "w", encoding="UTF-8")

# Escrever os resultados no arquivo, ordenados por frequência
for per, oco in sorted(all_per_words.items(), key=lambda x: x[1], reverse=True):
    print(f"{per}, {oco}", file=output)

# Fechar o arquivo de saída
output.close()
