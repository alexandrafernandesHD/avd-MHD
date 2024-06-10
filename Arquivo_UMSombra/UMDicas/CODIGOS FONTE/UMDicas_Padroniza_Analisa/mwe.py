#CÓDIGO PARA A EXTRAÇÃO DE MULTIPLE WORD EXPRESSIONS

#PARA IMPRIMIR A LINHA COMPLETA: 
'''with open('corpus-anotado_3-2-0.txt', 'r', encoding='utf-8') as arquivo_corpus:
    # Criar um arquivo para escrever as ocorrências desejadas
    with open('ocorrencias_desejadas.txt', 'w', encoding='utf-8') as arquivo_saida:
        # Iterar sobre as linhas do corpus
        for linha in arquivo_corpus:
            # Dividir a linha por tabulação
            partes = linha.strip().split('\t')
            # Verificar se a primeira parte tem duas ou mais palavras
            if len(partes) > 0 and len(partes[0].split()) >= 2:
                # Escrever a linha no arquivo de saída
                arquivo_saida.write(linha)'''

# PARA IMPRIMIR TERMO- CATEGORIA, IGNORANDO PERSON E PUNCT.
# Abrir o arquivo do corpus para leitura
with open('corpus-anotado_3-2-0.txt', 'r', encoding='utf-8') as arquivo_corpus:
    # Criar um arquivo para escrever os resultados desejados
    with open('mwe_1.txt', 'w', encoding='utf-8') as arquivo_saida:
        # Iterar sobre as linhas do corpus
        for linha in arquivo_corpus:
            # Dividir a linha por tabulação
            partes = linha.strip().split('\t')
            # Verificar se a primeira parte tem duas ou mais palavras
            if len(partes) >= 1 and len(partes[0].split()) >= 2:
                # Verificar se a última parte não é "PER" ou "PUNCT"
                if partes[-1] != "PER" and partes[-1] != "PUNCT":
                    # Escrever o primeiro, terceiro e quarto elementos no arquivo de saída
                    arquivo_saida.write(f"{partes[0]}\t{partes[-1]}\n")

