import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo CSV
caminho_arquivo = r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\UM_Dicas_Codes\corpus-anotado_4.csv"
dados = pd.read_csv(caminho_arquivo)

# Categorias gramaticais que queremos contar
categorias_gramaticais = ['DET', 'CCONJ', 'AUX', 'ADP', 'ADJ', 'ADV', 'NUM', 'PROPN', 'SCONJ', 'VERB', 'NOUN', 'PRON']

# Inicializa um dicionário para armazenar a contagem de cada categoria gramatical
contagem_categorias_gramaticais = {categoria: 0 for categoria in categorias_gramaticais}

# Percorre todas as colunas não nomeadas e conta as categorias gramaticais
for coluna in dados.columns[1:]:
    contagem_coluna = dados[coluna].value_counts()
    for categoria in categorias_gramaticais:
        if categoria in contagem_coluna.index:
            contagem_categorias_gramaticais[categoria] += contagem_coluna[categoria]

# Definição de cores para cada categoria gramatical
cores = ['skyblue', 'salmon', 'lightgreen', 'orange', 'purple', 'pink', 'yellow', 'red', 'blue', 'brown', 'grey', 'cyan']

# Plotagem do gráfico de barras com cores diferentes para cada categoria gramatical
plt.figure(figsize=(10, 6))
barras = plt.bar(contagem_categorias_gramaticais.keys(), contagem_categorias_gramaticais.values(), color=cores)

# Adiciona o número acima das barras
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval, int(yval), va='bottom', ha='center') # ha: horizontal alignment

plt.xlabel('Categorias Gramaticais')
plt.ylabel('Contagem')
plt.title('Contagem de Categorias Gramaticais')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
