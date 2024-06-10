import re

#CÓDIGO PARA ENCONTRAR AS DATAS POR ENTREVISTA

# Função para encontrar e contar datas em um texto
def encontrar_datas(texto):
    # Expressão regular para encontrar datas no formato dia de mês (com ou sem ano)
    padrao = r'\b\d{1,2}\s+de\s+(?:janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)(?:\s+de\s+\d{4})?\b'
    
    # Encontrar todas as correspondências usando a expressão regular
    datas_encontradas = re.findall(padrao, texto, flags=re.IGNORECASE)
    
    # Contar ocorrências de cada data
    contagem_datas = {}
    for data in datas_encontradas:
        # Normalizar datas para facilitar a contagem (converter para minúsculas)
        data_normalizada = data.lower()
        # Contar a ocorrência da data
        contagem_datas[data_normalizada] = contagem_datas.get(data_normalizada, 0) + 1
    
    return contagem_datas

# Função para processar um arquivo de texto com várias entrevistas
def processar_arquivo(arquivo_entrada, arquivo_saida):
    # Abrir o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        # Ler o conteúdo do arquivo
        conteudo = f.read()
    
    # Dividir o conteúdo do arquivo em entrevistas separadas
    entrevistas = conteudo.split('@UMDicas\\')
    
    # Abrir o arquivo de saída para escrever as contagens de datas
    with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
        # Para cada entrevista, encontrar e contar as datas
        for entrevista in entrevistas:
            if entrevista.strip():  # Ignorar strings vazias
                # Extrair o título da entrevista
                titulo_entrevista = entrevista.split('\n')[0].strip()
                # Encontrar e contar as datas na entrevista
                contagem_datas = encontrar_datas(entrevista)
                
                # Escrever o título da entrevista e a contagem das datas encontradas no arquivo de saída
                f_out.write(f"{titulo_entrevista}:\n")
                for data, contagem in contagem_datas.items():
                    f_out.write(f"data {data}: {contagem}\n")
                f_out.write("\n")

# Chamar a função para processar o arquivo "corpus-umsombra.txt" e escrever os resultados em um arquivo separado
processar_arquivo("corpus-umsombra.txt", "contagem_datas.txt")
