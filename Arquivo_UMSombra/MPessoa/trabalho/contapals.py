from jjcli import *
from collections import Counter

# Configurar o filtro de linha de comando
cl = clfilter("")

# Abrir o arquivo de saída
output = open("pals_ent.csv", "w", encoding="UTF-8")

# Iterar sobre o conteúdo do input
conteudo = ''.join(cl.input())
entrevistas = conteudo.split('@')

# Inicializar o contador para entrevistas
for i in range(1, len(entrevistas)):
    entrevista = entrevistas[i]
    palavras = entrevista.split()
    num_palavras = len(palavras)
    
    # Escrever o marcador e a contagem de palavras no arquivo de saída
    print(f"@ Entrevista {i}, {num_palavras} palavras", file=output)

# Fechar o arquivo de saída
output.close()
