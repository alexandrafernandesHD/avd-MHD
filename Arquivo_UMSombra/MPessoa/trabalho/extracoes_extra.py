import spacy
from collections import Counter

#15 palavras mais freuentes
# Carregar o modelo de linguagem português
nlp = spacy.load("pt_core_news_lg")

# Ler o conteúdo do arquivo
with open("corpus-umsombra.txt", 'r', encoding='UTF-8') as file:
    text = file.read()

# Processar o texto com SpaCy
doc = nlp(text)

# Filtrar as palavras que não são stopwords, não são pontuações e não são espaços em branco
words = [token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

# Contar a frequência das palavras
word_freq = Counter(words)

# Obter as 10 palavras mais frequentes
most_common_words = word_freq.most_common(15)

# Imprimir as 10 palavras mais frequentes
for word, freq in most_common_words:
    print(f'{word}: {freq}')




 