from jjcli import *
import re

# Obtém todos os arquivos .md na pasta corpus
docs = glob("corpus/*.md")

# Ordena os arquivos e configura o filtro de linha de comando
cl = clfilter("")
cl.args = sorted(docs)

# Abre o arquivo de saída
out = open("metadados.txt", 'w', encoding="UTF-8")

# Itera sobre o conteúdo dos arquivos
for txt in cl.text():
    # Encontra o conteúdo entre `---` e `---`
    metadados = re.findall(r'---(.*?)---', txt, flags=re.S)
    
    for meta in metadados:
        # Escreve o nome do arquivo e os metadados extraídos no arquivo de saída
        print(f"---\n{meta.strip()}\n---\n", file=out)

# Fecha o arquivo de saída
out.close()
