import pandas as pd
import matplotlib.pyplot as plt

# Aumenta o tamanho da fonte
plt.rcParams.update({'font.size': 14})

# Carrega o arquivo CSV
caminho_arquivo = r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\UM_Dicas_Codes\corpus-anotado_4.csv"
dados = pd.read_csv(caminho_arquivo)

# Categorias que queremos contar
categorias = ['PER', 'LOC', 'ORG', 'MISC']

# Inicializa um dicionário para armazenar a contagem de cada categoria
contagem_categorias = {categoria: 0 for categoria in categorias}

# Percorre todas as colunas não nomeadas e conta as categorias
for coluna in dados.columns[1:]:
    contagem_coluna = dados[coluna].value_counts()
    for categoria in categorias:
        if categoria in contagem_coluna.index:
            contagem_categorias[categoria] += contagem_coluna[categoria]

# Definição de cores para cada categoria
cores = ['skyblue', 'salmon', 'lightgreen', 'orange']

# Plotagem do gráfico de barras com cores diferentes para cada categoria
plt.figure(figsize=(10, 6))
barras = plt.bar(contagem_categorias.keys(), contagem_categorias.values(), color=cores)

# Adiciona o número acima das barras
for barra in barras:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2.0, yval, int(yval), va='bottom', ha='center') # va: vertical alignment

plt.xlabel('Categorias')
plt.ylabel('Contagem')
plt.title('Contagem de Categorias (PER, LOC, ORG, MISC)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
