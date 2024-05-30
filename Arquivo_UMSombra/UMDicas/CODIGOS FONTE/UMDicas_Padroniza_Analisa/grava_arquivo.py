import os

def grava_resultado(texto,nome_arquivo,modo,pasta_destino):

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    with open(pasta_destino+"/"+nome_arquivo,modo, encoding="utf-8") as saida:
        if isinstance(texto,str):
            saida.write(texto)
        else:
            if isinstance(texto,list):
                for linha in texto:
                    saida.write(str(linha)+"\n")