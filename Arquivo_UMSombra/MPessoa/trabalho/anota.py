import spacy
from jjcli import *

# Certifique-se de instalar e carregar o modelo de linguagem português do SpaCy
# pip install -U spacy
# python -m spacy download pt_core_news_lg

# Carregar o tokenizador, tagger, parser e NER do modelo português
nlp = spacy.load("pt_core_news_lg")

# Configurar o filtro de linha de comando
cl = clfilter("")

# Contador de parágrafos

# Abrir arquivo de saída para escrever os resultados
output = open("corpus-anotado.txt", 'w', encoding="UTF-8")

# Iterar sobre cada parágrafo
for par in cl.paragraph():
    # Processar o parágrafo com SpaCy
    doc = nlp(par)
    
    # Fundir entidades nomeadas em tokens únicos
    with doc.retokenize() as retokenizer:
        for entity in doc.ents:
            retokenizer.merge(entity)
    
    # Iterar sobre cada sentença no documento
    for sentence in doc.sents:
        print(file=output)  # Adiciona uma nova linha no arquivo de saída
        
        # Iterar sobre cada palavra na sentença
        for word in sentence:
            if word.is_space:
                continue  # Pular espaços em branco
            if word.pos_ == "PUNCT":
                continue  # Pular pontuações
            
            # Escrever detalhes da palavra no arquivo de saída
            print(f'{word.text}\t{word.lemma_}\t{word.pos_}\t{word.ent_type_}', file=output)
