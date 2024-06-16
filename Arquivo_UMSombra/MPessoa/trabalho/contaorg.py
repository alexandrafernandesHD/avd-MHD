import spacy
from jjcli import *
from collections import Counter

# Configurar o filtro de linha de comando
cl = clfilter("")
all_org_words = Counter()

# Iterar sobre cada linha do input
for linha in cl.input():
    if "ORG" in linha:
        # Dividir a linha no primeiro TAB e pegar a primeira parte
        primeira_parte = linha.split('\t')[0]
        # Atualizar o contador com a primeira parte da linha
        all_org_words.update([primeira_parte])

# Abrir o arquivo de saída para escrever os resultados
output = open("org.csv", "w", encoding="UTF-8")

# Escrever os resultados no arquivo, ordenados por frequência
for org, oco in sorted(all_org_words.items(), key=lambda x: x[1], reverse=True):
    print(f"{org}, {oco}", file=output)

# Fechar o arquivo de saída
output.close()
