import re
import openpyxl

def le_livro(nome_livro):
    with open(nome_livro, encoding="utf-8") as arquivo_livro:
        livro = arquivo_livro.read()
    return livro.split('@')  # Quebra o conteúdo do livro por "@", utilizado para sinalizar um novo soneto

def carrega_lexico():
    dicionario_lexico = {}
    
    with open("sentilexjj.txt", encoding="utf-8") as learquivo:
        for linha in learquivo:
            if linha.strip():
                partes = linha.strip().split(';')
                palavra_info = partes[0].split(',')
                palavra = palavra_info[0]
                for parte in partes:
                    if 'POL:N0=' in parte:
                        polaridade = int(parte.split('=')[1])
                        dicionario_lexico[palavra] = polaridade

    return dicionario_lexico

def analisa_entrevistas(entrevistas, dicionario):
    resultados = []
    for n, entrevista in enumerate(entrevistas):
        positivas = 0
        negativas = 0

        for word, sentiment in dicionario.items():
            quantidade = len(re.findall(r'\b' + re.escape(word) + r'\b', entrevista, flags=re.IGNORECASE))
            if sentiment > 0:
                positivas += quantidade
            else:
                negativas += quantidade

        resultados.append((f"Entrevista {n + 1}", positivas, negativas))
    return resultados

def salva_resultados_texto(resultados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
        for soneto, positivas, negativas in resultados:
            arquivo.write(f"{soneto}: Positivas = {positivas}, Negativas = {negativas}\n")

def salva_resultados_excel(resultados, nome_arquivo):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Entrevistas", "Positivas", "Negativas"])
    
    for soneto, positivas, negativas in resultados:
        ws.append([soneto, positivas, negativas])
    
    wb.save(nome_arquivo)

# Carrega as entrevistas do arquivo
entrevistas = le_livro("corpus-umsombra.txt")

# Carrega o léxico de sentimentos
dicionario = carrega_lexico()

# Analisa os entrevistas
resultados = analisa_entrevistas(entrevistas, dicionario)

# Salva os resultados em um arquivo de texto
salva_resultados_texto(resultados, "sentimento_sentillex.txt")

# Salva os resultados em um arquivo Excel
salva_resultados_excel(resultados, "analisesentimentos.xlsx")
