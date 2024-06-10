import spacy
import matplotlib.pyplot as plt


# Carregando o modelo do SpaCy para o idioma desejado (exemplo: português)
nlp = spacy.load("pt_core_news_lg")


def count_stopwords(text):
    tokens = text.split("\t")
    if len(tokens) >= 3:  # Verifica se há pelo menos três colunas (a primeira para identificação, a segunda para a palavra, a terceira para a categoria gramatical)
        word = tokens[1].lower()  # Pegando a palavra e colocando em minúsculas
        pos_tag = tokens[2]  # Pegando a categoria gramatical
        if pos_tag in ["ADP", "CCONJ", "PUNCT", "NUM", "SCONJ"]:  # Verificando se a categoria gramatical está na lista de stopwords
            return 1
    return 0

corpus_entrevistas = "corpus-anotado_3-2-0.txt"

# Lendo o conteúdo do arquivo e dividindo-o em textos individuais
with open(corpus_entrevistas, "r", encoding="utf-8") as file:
    textos_entrevistas = file.readlines()

# Contadores para stopwords e outras palavras
total_stopwords = 0
total_words = 0

# Processar cada texto de entrevista no corpus
for entrevista in textos_entrevistas:
    stopwords_count = count_stopwords(entrevista)
    total_stopwords += stopwords_count
    total_words += 1  # Contando o número total de palavras como 1 por linha

# Calcular a porcentagem de stopwords e outras palavras
stopwords_percentage = (total_stopwords / total_words) * 100
other_words_percentage = 100 - stopwords_percentage

# Exibir resultados
print("Porcentagem de stopwords:", stopwords_percentage)
print("Porcentagem de outras palavras:", other_words_percentage)


# Porcentagens
stopwords_percentagem = 31.554051105583714
outras_palavras_percentagem = 68.44594889441629


# Nomes das categorias
categorias = ['Stopwords', 'Outras Palavras']

# Porcentagens arredondadas para uma casa decimal
porcentagens = [round(stopwords_percentagem, 1), round(outras_palavras_percentagem, 1)]

# Cores
cores = ['#ff9999','#66b3ff']

# Plot
plt.figure(figsize=(8, 6))
plt.pie(porcentagens, labels=categorias, colors=cores, autopct='%1.1f%%', startangle=140)
plt.title('Porcentagem de Stopwords vs Outras Palavras')
plt.axis('equal')  
plt.show()
