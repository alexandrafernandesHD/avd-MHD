import csv

# Dicionários de normalização
mapa =  { "Fernando Parente": "Fernando Parente",
    "Dr. Fernando Parente": "Fernando Parente",
    "Professor Fernando Parente": "Fernando Parente",
    "Pró-Reitor Luís Amaral": "Luís Amaral",
    "Luís Amaral": "Luís Amaral",
    "Roque Teixeira": "Roque Teixeira",
    "*Roque Teixeira": "Roque Teixeira",
    "Manuel João Costa Pró-reitor": "Manuel João Costa",
    "Manuel João Costa": "Manuel João Costa",
    "Engº Carlos Silva": "Carlos Silva",
    "Eng.º Carlos Silva": "Carlos Silva",
    "Engª. Carlos Silva": "Carlos Silva",
    "Carlos Silva": "Carlos Silva",
    "CARLOS SILVA": "Carlos Silva",
    "Dicas- Carlos Santos": "Carlos Santos",
    "Carlos Alberto Videira": "Carlos Videira",
    "Carlos Videira": "Carlos Videira",
    "Lloyd Braga": "Residência Lloyd de Braga",
    "Residência Lloyd Braga": "Residência Lloyd de Braga",
    "Lloyd de Braga": "Residência Lloyd de Braga",
    "Lloyd": "Residência Lloyd de Braga",
    "Irene Montenegro": "Irene Montenegro",
    "Profª Irene Montenegro": "Irene Montenegro",
    "Pró-Reitora Irene Montenegro": "Irene Montenegro",
}
input_csv = "person.csv"
output_csv = "umd_pessoa.csv"

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
