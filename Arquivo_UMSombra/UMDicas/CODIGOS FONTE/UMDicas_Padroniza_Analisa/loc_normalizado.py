import csv

# Dicionários de normalização
mapa = {
    "Universidade do Minho": "Universidade do Minho",
    "Universidade": "Universidade do Minho",
    "Reitor da UMinho": "Universidade do Minho",
    "Reitor da Universidade do Minho": "Universidade do Minho",
    "Universidades": "Universidade do Minho",
    "Novembro do Reitor da Universidade do Minho": "Universidade do Minho",
    "U.Minho": "Universidade do Minho",
    "Escolas da Universidade do Minho": "Universidade do Minho",
    "universidade do minho": "Universidade do Minho",
    "Remodelação das Cantinas do Campus de Azurém": "Universidade do Minho - Campus de Azurém",
    "Remodelação das Cantinas de Azurém": "Universidade do Minho - Campus de Azurém",
    "Residência de Azurém": "Universidade do Minho - Campus de Azurém",
    "Campus de Azurém": "Universidade do Minho - Campus de Azurém",
    "Residências de Azurém": "Universidade do Minho - Campus de Azurém",
    "Complexo de Azurém": "Universidade do Minho - Campus de Azurém",
    "Engenharia de Azurém": "Universidade do Minho - Campus de Azurém",
    "Residência Universitária de Azurém": "Universidade do Minho - Campus de Azurém",
    "Complexos Desportivos de Azurém": "Universidade do Minho - Campus de Azurém",
    "Armazém de Azurém": "Universidade do Minho - Campus de Azurém",
    "Bar do Auditório de Azurém": "Universidade do Minho - Campus de Azurém",
    "Bar Académico de Braga": "Bar Académico",
    "Bar Académico": "Bar Académico",
    "MELHOR ACADEMIA DO PAÍS": "Universidade do Minho",
    "universidade do Minho": "Universidade do Minho",
    "ULisboa": "Universidade de Lisboa",
    "Univ de Lisboa": "Universidade de Lisboa",
    "Universidade de Lisboa": "Universidade de Lisboa",
    "Belas-Artes de Lisboa": "Universidade de Lisboa",
    "ISEGI/ Universidade Nova de Lisboa": "Universidade Nova de Lisboa",
    "Universidade Nova de Lisboa": "Universidade Nova de Lisboa",
    "Nova de Lisboa": "Universidade Nova de Lisboa",
    "Remodelação das Residências do Campus de Azurém": "Universidade do Minho - Campus de Azurém"
}

# Arquivo de entrada
input_csv = "loc_1.csv"
output_csv = "umd_locs"

# Normalizar nomes e contar quantidades
quantidades_normalizadas = {}
with open(input_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) >= 2:
            nome = " ".join([part.strip() for part in row[:-1]])
            quantidade = int(row[-1])
            nome_normalizado = mapa.get(nome, nome)
            quantidades_normalizadas[nome_normalizado] = quantidades_normalizadas.get(nome_normalizado, 0) + quantidade

# Escrever no arquivo CSV
with open(output_csv, "a", encoding="utf-8", newline='') as outfile:
    csvwriter = csv.writer(outfile)
    #csvwriter.writerow(["Nome", "Quantidade"])
    for nome, quantidade in quantidades_normalizadas.items():
        csvwriter.writerow([nome, quantidade])
