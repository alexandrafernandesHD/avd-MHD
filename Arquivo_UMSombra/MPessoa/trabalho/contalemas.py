import spacy 
from jjcli import *
from collections import Counter

# Carregar o modelo de linguagem do spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Obter a lista de stopwords
stopwords = nlp.Defaults.stop_words

cl = clfilter("")
all_lemas = Counter()
for linha in cl.input():
    palavras = linha.split()
    if len(palavras) >= 3:
        lema = palavras[1]
        # Verificar se a palavra não é uma stopword
        if lema.lower() not in stopwords:
            all_lemas.update([lema]) 

# Abrir o arquivo de saída
output = open("lemas.csv", "w", encoding="UTF-8")

# Ordenar os verbos pelo número de ocorrências (decrescente)
for lema, oco in sorted(all_lemas.items(), key=lambda x: x[1], reverse=True):
    print(f"{lema}, {oco}", file=output)

# Fechar o arquivo de saída
output.close()
