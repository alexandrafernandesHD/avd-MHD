from textblob import TextBlob

# Função para extrair texto de um arquivo .txt
def extrair_texto_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

# Função para analisar o sentimento de um texto
def analisar_sentimento_texto(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment
    return sentimento

# Função para dividir o texto em entrevistas
def dividir_entrevistas(texto):
    entrevistas = texto.split('@')
    # Remove entradas vazias se houver
    entrevistas = [entrevista.strip() for entrevista in entrevistas if entrevista.strip()]
    return entrevistas

# Caminho para o arquivo .txt
caminho_txt = "corpus_ingles.txt"

# Extrair texto do arquivo .txt
texto_txt = extrair_texto_txt(caminho_txt)

# Dividir o texto em entrevistas
entrevistas = dividir_entrevistas(texto_txt)

# Realizar análise de sentimentos para cada entrevista
resultados_entrevistas = {}
for i, entrevista in enumerate(entrevistas):
    sentimento = analisar_sentimento_texto(entrevista)
    resultados_entrevistas[f'Entrevista {i+1}'] = sentimento

# Exibir resultados
for entrevista, sentimento in resultados_entrevistas.items():
    print(f"{entrevista}:")
    print(f"  Sentimento: {sentimento}\n")

# Opcional: Salvar resultados em um arquivo
with open("sentimento_textblob.txt", "w", encoding="utf-8") as arquivo_saida:
    for entrevista, sentimento in resultados_entrevistas.items():
        arquivo_saida.write(f"{entrevista}:\n")
        arquivo_saida.write(f"  Sentimento: {sentimento}\n\n")
