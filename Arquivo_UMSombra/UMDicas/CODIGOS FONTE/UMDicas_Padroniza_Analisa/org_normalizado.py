import csv

# Dicionários de normalização
mapa =  {
    "UMinho?": "Universidade do Minho",
    "UMinho": "Universidade do Minho",
    "Academia": "Universidade do Minho",
    "Academia Minhota": "Universidade do Minho",
    "U.M.": "Universidade do Minho",
    "U.M.?": "Universidade do Minho",

    "AAUMinho": "AAUM",
    "AAUM": "AAUM",
    "Associação Académica": "AAUM",
    "Associação Académica da Universidade do Minho": "AAUM",
    "AAUM?": "AAUM",
    "AAEUM": "AAUM",

        "Departamento Desportivo e Cultural": "Departamentos dos SASUM",
    "Departamento Alimentar": "Departamentos dos SASUM",
    "Departamento Financeiro": "Departamentos dos SASUM",
    "Departamento": "Departamentos dos SASUM",
    "Departamento Desportivo e Cultural?": "Departamentos dos SASUM",
    "Departamento?": "Departamentos dos SASUM",
    "Departamento Administrativo e Financeiro dos SASUM": "Departamentos dos SASUM",
    "Departamento Administrativo": "Departamentos dos SASUM",
    "Departamento Social dos SASUM": "Departamentos dos SASUM",
    "Departamento Social": "Departamentos dos SASUM",
    "Diretora de Serviços do Departamento Administrativo": "Departamentos dos SASUM",
    "Departamento Administrativo e Financeiro": "Departamentos dos SASUM",
    "Diretora do Departamento de Apoio Social": "Departamentos dos SASUM",
    "Departamento de Apoio Social": "Departamentos dos SASUM",
    "Diretora do Departamento Alimentar": "Departamentos dos SASUM",
    "Departamento de Apoio Social dos SASUM": "Departamentos dos SASUM",
    "Secretariado do Departamento de Apoio Social": "Departamentos dos SASUM",
    "Departamento de Desporto e Cultura dos SASUM": "Departamentos dos SASUM",
    "Setor de Secretariado do Departamento de Apoio Social dos SASUM": "Departamentos dos SASUM",
    "Setor de Secretariado do Departamento de Apoio Social?": "Departamentos dos SASUM",
    "Setor de Secretariado do Departamento de Apoio Social": "Departamentos dos SASUM",
    "Departamento de Sistemas de Informação da Universidade do Minho": "Departamentos dos SASUM",
    "Departamento de Produção e Sistemas": "Departamentos dos SASUM",
    "Desportiva do Departamento Desportivo e Cultural dos SASUM": "Departamentos dos SASUM",
    "Departamento Desportivo e Cultural dos SASUM": "Departamentos dos SASUM",
    "Departamento Desportivo": "Departamentos dos SASUM",
    "Vice-Presidente do Departamento Desportivo": "Departamentos dos SASUM",
    "Departamento Desportivo e Cultural da Universidade do Minho": "Departamentos dos SASUM",
    "Diretor do Departamento Desportivo e Cultural": "Departamentos dos SASUM",
    "Diretora do Departamento Financeiro": "Departamentos dos SASUM",
    "Diretora do Departamento Apoio Social": "Departamentos dos SASUM",
    "Setores do Departamento": "Departamentos dos SASUM",
    "Departamento Apoio Social": "Departamentos dos SASUM",
    "Secretariado do Departamento Alimentar dos SASUM": "Departamentos dos SASUM",
    "Sector de Secretariado do Departamento Alimentar dos SASUM": "Departamentos dos SASUM",
    "Departamento Alimentar dos SASUM": "Departamentos dos SASUM",
    "Secretariado deste Departamento": "Departamentos dos SASUM",
    "Sector de Secretariado do Departamento Alimentar?": "Departamentos dos SASUM",
    "Departamento Desportivo e Cultural dos Serviços de Ação Social": "Departamentos dos SASUM",
    "Departamento Alimentar dos Serviços de Acção Social da Universidade do Minho": "Departamentos dos SASUM",
    "Departamento Contabilístico e Financeiro": "Departamentos dos SASUM",
    "Sistema de Gestão da Qualidade do Departamento Contabilístico e Financeiro": "Departamentos dos SASUM",
    "Departamento Desportivo e Cultural dos Serviços de Accão Social da Universidade do Minho": "Departamentos dos SASUM",
    "Divisão de Alojamento do Departamento de Apoio Social": "Departamentos dos SASUM",
    "Departamento de Apoio": "Departamentos dos SASUM",
    "Departamento Contabilístico e Financeiro dos SASUM": "Departamentos dos SASUM",
    "Directora do Departamento Recreativo e Cultural": "Departamentos dos SASUM",
    "Departamentos Alimentar": "Departamentos dos SASUM",
    "Departamento dos Serviços de Acção Social": "Departamentos dos SASUM",
    "Departamentos dos Serviços de Acção Social": "Departamentos dos SASUM",
    "Departamentos dos Serviços de Acção Social da Universidade do Minho": "Departamentos dos SASUM",
    "Unidades do Departamento Alimentar": "Departamentos dos SASUM",
    "Departamento Alimentar?": "Departamentos dos SASUM",
    "Chefe de Divisão do Departamento Social dos SASUM": "Departamentos dos SASUM",
    "Departamento Social?": "Departamentos dos SASUM",
    "Departamento Social – Bolsas": "Departamentos dos SASUM",
    "Actividades do Departamento Desportivo e Cultural": "Departamentos dos SASUM",
    "Director do Departamento Desportivo de Braga": "Departamentos dos SASUM",
    "Director do Departamento Despor": "Departamentos dos SASUM",
    "Sector de Secretariado Departamento Alimentar dos SASUM": "Departamentos dos SASUM",
    "Sector de Secretariado do Departamento Alimentar": "Departamentos dos SASUM",
    "Departamento Alimentar dos Serviços de Acção Social da UMinho": "Departamentos dos SASUM",
    "Departamento Desportivo da AAUMinho?": "Departamentos dos SASUM"
    
}
input_csv = "org.csv"
output_csv = "umd_org.csv"

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
