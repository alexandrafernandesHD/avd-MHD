import csv

# Dicionários de normalização
mapa = {
    # UMDicas
    "Jornal UMdicas": "UMDicas",
    "UMdicas": "UMDicas",
    "UMDicas": "UMDicas",
    "O UMdicas": "UMDicas",
    
    # Ação Social
    "Administrador dos SASUM": "Ação Social",
    "Ação Social": "Ação Social",
    
    # TUTORUM
    "Programa Tutorum": "TUTORUM",
    "Programa TUTORUM?": "TUTORUM",
    "TUTORUM?": "TUTORUM",
    "TUTORUM": "TUTORUM",
    
    # Enterro da Gata
    "Monumentais Festas do Enterro da Gata": "Enterro da Gata",
    "Enterro da Gata": "Enterro da Gata",
    "Enterro": "Enterro da Gata",
    "Serenata do Enterro da Gata": "Enterro da Gata",
    "Enterro da Gata da Universidade do Minho": "Enterro da Gata",
    "MONUMENTAIS FESTAS DO ENTERRO DA GATA*": "Enterro da Gata",
    "O Enterro da Gata": "Enterro da Gata",
    "Enterro deste ano": "Enterro da Gata",
    
    # Licenciaturas
    "Licenciatura em Biologia-Geologia": "Licenciaturas",
    "Licenciatura em Biologia-Geologia?": "Licenciaturas",
    "Licenciatura em": "Licenciaturas",
    "Licenciatura em Bioquímica": "Licenciaturas",
    "Licenciatura em Línguas e Literaturas Europeias?": "Licenciaturas",
    "Licenciatura em Línguas e Literaturas Europeias": "Licenciaturas",
    "Licenciatura em Matemática": "Licenciaturas",
    "Estudei Matemática": "Licenciaturas",
    "Licenciatura em Matemática?": "Licenciaturas",
    "Licenciatura em Matemática e Ciências Computação": "Licenciaturas",
    "Licenciaturas": "Licenciaturas",
    "Programa de Licenciaturas Internacionais": "Licenciaturas",
    "Licenciatura em Economia": "Licenciaturas",
    "Licenciatura em Física": "Licenciaturas",
    "Física Médica": "Licenciaturas",
    "Licenciatura em Física": "Licenciaturas",
    "Licenciatura": "Licenciaturas",
    "Licenciado em Física": "Licenciaturas",
    "Licenciados em Física": "Licenciaturas",
    "Física e Matemática": "Licenciaturas",
    "Licenciatura em Estatística Aplicada": "Licenciaturas",
    "Licenciatura em Design e Marketing de Moda": "Licenciaturas",
    "Licenciatura em Bioquímica": "Licenciaturas",
    "Terminei a Licenciatura em Engenharia do Vestuário": "Licenciaturas",
    "Licenciatura em Medicina": "Licenciaturas",
    "Licenciatura em Estudos Orientais": "Licenciaturas",
    "Curso de Licenciatura em Enfermagem": "Licenciaturas",
    "Relações Internacionais": "Licenciaturas",
    
    # Mestrados/Mestrados Integrados
    "Mestrado Integrado em Engenharia Mecânica": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado Engenharia Têxtil?": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Arquitetura": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Arquitectura": "Mestrados/Mestrados Integrados",
    "Mestrado em Direitos Humanos": "Mestrados/Mestrados Integrados",
    "Mestrado em Matemática": "Mestrados/Mestrados Integrados",
    "Mestrado em Matemática e Computação": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Engenharia Biológica": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado": "Mestrados/Mestrados Integrados",
    "Mestrado": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Engenharia": "Mestrados/Mestrados Integrados",
    "Projeto Individual ou Dissertação de Mestrado": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Psicologia": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Medicina": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Engenharia Biomédica": "Mestrados/Mestrados Integrados",
    "Dissertações de Mestrado": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado em Engenharia de Telecomunicações e Informática": "Mestrados/Mestrados Integrados",
    "Mestrado Integrado de Eletrónica": "Mestrados/Mestrados Integrados",
    "Mestrados Integrados": "Mestrados/Mestrados Integrados",
    
    # Erasmus
    "Erasmus Students Network Minho": "Erasmus",
    "Erasmus": "Erasmus",
    "Coordenador Erasmus": "Erasmus",
    "programa Erasmus": "Erasmus",
    "Programa Erasmus": "Erasmus",
    "Erasmus Mundus": "Erasmus",
    "ERASMUS": "Erasmus",
    "Erasmus?": "Erasmus",
    "ERASMUS?": "Erasmus",
    "Madrinho Erasmus": "Erasmus",
    "Mestrados Erasmus Mundus": "Erasmus",
    
    # Campeonatos Desportivos Universitários
    "Campeonato Mundial Universitário de Xadrez": "Campeonatos Desportivos Universitários",
    "Campeonatos Mundiais Universitários de Xadrez": "Campeonatos Desportivos Universitários",
    "Campeonato Europeu de Taekwondo": "Campeonatos Desportivos Universitários",
    "Campeonato Mundial Universitário de Andebol": "Campeonatos Desportivos Universitários",
    "Campeonato Mundial Universitário": "Campeonatos Desportivos Universitários",
    "Campeonatos Nacionais Universitários": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário": "Campeonatos Desportivos Universitários",
"Campeonato Nacional da 1ª Divisão": "Campeonatos Desportivos Universitários",
"Campeonatos": "Campeonatos Desportivos Universitários",
"Campeonato do Mundo Universitário": "Campeonatos Desportivos Universitários",
"Campeonatos Europeus Universitários": "Campeonatos Desportivos Universitários",
"Campeonatos Nacionais Universitários Individuais Concentrados": "Campeonatos Desportivos Universitários",
"Campeonato Mundial Universitário de Andebol 2014": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Taekwondo": "Campeonatos Desportivos Universitários",
"Campeonato Nacional de Seniores": "Campeonatos Desportivos Universitários",
"Campeonato": "Campeonatos Desportivos Universitários",
"Campeonato Mundial": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Andebol": "Campeonatos Desportivos Universitários",
"Campeonato da Europa": "Campeonatos Desportivos Universitários",
"Tetra campeonato": "Campeonatos Desportivos Universitários",
"Campeonato do Mundo": "Campeonatos Desportivos Universitários",
"Campeonatos Mundiais Universitários de Futsal": "Campeonatos Desportivos Universitários",
"Campeonatos Mundiais da FISU": "Campeonatos Desportivos Universitários",
"Final do Campeonato da Europa": "Campeonatos Desportivos Universitários",
"Campeonato Mundial Universitário de Futsal": "Campeonatos Desportivos Universitários",
"Campeonatos Europeus": "Campeonatos Desportivos Universitários",
"Campeonato Mundial Universitário de Ciclismo": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Futsal": "Campeonatos Desportivos Universitários",
"Campeonato do Mundo Universitário de Ciclismo": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Voleibol": "Campeonatos Desportivos Universitários",
"Campeonato Europeu": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Futsal a Braga": "Campeonatos Desportivos Universitários",
"Campeonatos Mundial de Ciclismo": "Campeonatos Desportivos Universitários",
"Campeonato Mundial Universitário de Futsal 2022": "Campeonatos Desportivos Universitários",
"Campeonato Nacional Universitário de Judo": "Campeonatos Desportivos Universitários",
"Campeonato Europeu de Voleibol Universitário": "Campeonatos Desportivos Universitários",
"Campeonato Mundial de Futsal Universitário": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Voleibol 2023": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Júnior": "Campeonatos Desportivos Universitários",
"Campeonato Nacional": "Campeonatos Desportivos Universitários",
"Campeonato Nacional Universitário": "Campeonatos Desportivos Universitários",
"Campeonato Europeu Universitário de Basquetebol": "Campeonatos Desportivos Universitários",
"Campeonatos Europeus de Juniores Femininos": "Campeonatos Desportivos Universitários",
"Campeonato Europeu B de Seniores Femininos": "Campeonatos Desportivos Universitários",
"Campeonato da Europa de corta-mato": "Campeonatos Desportivos Universitários",
"Campeonato do Mundo de corta-mato": "Campeonatos Desportivos Universitários",
"Campeonatos do Mundo": "Campeonatos Desportivos Universitários",
"Campeonato Mundial Universitário de Badminton": "Campeonatos Desportivos Universitários",
"Melhor Campeonato do Mundo Universitário": "Campeonatos Desportivos Universitários",
"Campeonato Mundial de Badminton": "Campeonatos Desportivos Universitários",
"Campeonato Nacional Universitário de Pista ao Ar": "Campeonatos Desportivos Universitários",
"I Campeonato Europeu Universitário de Taekwondo": "Campeonatos Desportivos Universitários",
"Campeonato da Europa de Sub-21": "Campeonatos Desportivos Universitários",
"Campeonato Europeu de Juniores": "Campeonatos Desportivos Universitários",
"Campeonatos nacionais Universitários": "Campeonatos Desportivos Universitários",
"campeonato do Mundo": "Campeonatos Desportivos Universitários",
"Campeonato Nacional de Futsal": "Campeonatos Desportivos Universitários",
"Campeonato Nacional de Futsal da 2ª Divisão": "Campeonatos Desportivos Universitários",
"Campeonatos do Mundo de Futsal": "Campeonatos Desportivos Universitários",
"Campeonato da Europa de Maratonas": "Campeonatos Desportivos Universitários"
}

input_csv = "misc.csv"
output_csv = "umd_misc.csv"

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

