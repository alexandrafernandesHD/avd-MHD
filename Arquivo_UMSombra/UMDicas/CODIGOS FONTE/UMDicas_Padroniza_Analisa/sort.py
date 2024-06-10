import csv
from collections import Counter

#CÓDIGO UTILIZADO PARA ORDENAR VALORES NO CSV, COM MAIS FREQUENCIAS PARA MENOS


# Caminho do arquivo de entrada e saída
input_file_path = 'C:\\Users\\Cristiana Gomes\\Desktop\\csv_prontos\\umd_nome.csv'
output_file_path = 'umd_nome_1.csv'

# Dicionário para armazenar a contagem de organizações
organizacoes_contagem = Counter()

# Ler o arquivo CSV de entrada e contar as ocorrências das organizações
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        organizacao = row[0].strip()
        frequencia_str = row[1].strip()
        if frequencia_str.isdigit():
            frequencia = int(frequencia_str)
            organizacoes_contagem[organizacao] += frequencia
        else:
            print(f"Erro: Valor inválido de frequência na linha {row}")

# Classificar as organizações por frequência em ordem decrescente
organizacoes_frequentes = sorted(organizacoes_contagem.items(), key=lambda x: x[1], reverse=True)

# Escrever as organizações frequentes no arquivo de saída
with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Organização', 'Frequência'])
    for organizacao, frequencia in organizacoes_frequentes:
        writer.writerow([organizacao, frequencia])

print("Organizações frequentes foram salvas em", output_file_path)