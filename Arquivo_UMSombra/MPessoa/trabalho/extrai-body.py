from jjcli import *
import re

# Obtém todos os arquivos .md na pasta corpus
docs = glob("corpus/*.md")

# Ordena os arquivos e configura o filtro de linha de comando
cl = clfilter("")
cl.args = sorted(docs)

# Abre o arquivo de saída
out = open("corpus-umsombra.txt", 'w', encoding="UTF-8")

# Itera sobre o conteúdo dos arquivos
for txt in cl.text():
    # Remove o conteúdo entre `---` e `---`, incluindo as próprias linhas `---`
    txt = re.sub(r'---.*?---', '', txt, flags=re.S)
    
    # Remove linhas que começam com TAG, versao, episodio, termo, tipo, onde, quando, numerofilhos
    lines = txt.split('\n')
    filtered_lines = [
        line for line in lines 
        if not re.match(r'^(TAG|versao|episodio|termo|tipo|onde|quando|numerofilhos)', line, flags=re.I)
    ]
    
    # Remove tags HTML
    filtered_lines = [re.sub(r'<.*?>', '', line) for line in filtered_lines]
    
    # Junta as linhas filtradas de volta em uma única string
    body = '\n'.join(filtered_lines)
    
    # Escreve o nome do arquivo seguido do conteúdo processado
    print(f"@{cl.filename()}\n", body.strip(), file=out)

# Fecha o arquivo de saída
out.close()
