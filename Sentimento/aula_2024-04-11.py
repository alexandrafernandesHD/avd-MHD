import re
import subprocess

def le_livro(nome_livro):
    with open (nome_livro, encoding="utf-8") as arquivo_livro:
        livro=arquivo_livro.read()#Carrega o conteúdo completo do livro para a variável livro
    return livro.split('#')#Quebra o conteúdo o livro por "#", utilizado para sinalizar um novo capítulo

def analisa_capitulos(capitulos):
        
    dicionario=carrega_lexico()
        
    for n,capitulo in enumerate(capitulos):
        positivas=0
        negativas=0
        
        print("-"*50)
        for word in dicionario:
            quantidade=len(re.findall(word,capitulo))
            if dicionario[word]>0:
                positivas+=quantidade
            else:
                negativas+=quantidade
        print(f"Capitulo {n}: Positivas: {positivas} - Negativas: {negativas}")
            #print(f"{word} ({dicionario[word]}): {quantidade}")
            
            
def carrega_lexico():
    with open("positivos.txt", encoding="utf-8") as learquivo:
        positivos=learquivo.read().splitlines()
    with open("negativos.txt", encoding="utf-8") as learquivo:
        negativos=learquivo.read().splitlines()
            
    dicionario_lexico={x:1 for x in positivos} | {x:-1 for x in negativos}#Forma um dicionario lexico com as palavras dos arquivos positivos e negativos
        
    return(dicionario_lexico)


capitulos=le_livro("HP.txt")
print(len(capitulos))
analisa_capitulos(capitulos)       
            
"""
    def analisa_capitulos_v0(capitulos):
        #Tentativa 3:
        #A mais 'fácil': trabalhar com um arquivo de texto para cada capítulo
        for capitulo in capitulos:
            num_capitulo=capitulo.splitlines()[0].replace(" ","")
            if not num_capitulo.isupper():
                num_capitulo="_INTRO"
            with open (f"HP-Cap_{num_capitulo}.txt", "w", encoding="utf-8") as arquivo_capitulo:
                arquivo_capitulo.write("---\n")
                arquivo_capitulo.write(capitulo)
            
            def busca_palavras(tipo):
                comando = f'rg -o -w -f {tipo}.txt HP-Cap_{num_capitulo}.txt'
                lista=subprocess.run(comando,shell=True, capture_output=True, text=True)
                resultado=(str(lista)).split()
                resultados=((resultado[7].split("'")[1])[:]).split("\\n")
                palavras_capitulo={}
                for resultado in resultados:
                    if resultado!="":
                        if resultado in palavras_capitulo:
                            palavras_capitulo[resultado]+=1
                        else:
                            palavras_capitulo[resultado]=1
                palavras_capitulo=dict(sorted(palavras_capitulo.items(), key=lambda item: item[1], reverse=True))
                with open (f"HP-Cap_{num_capitulo}.txt", "r", encoding="utf-8") as arquivo_capitulo:
                    texto_original=arquivo_capitulo.read()
                    with open (f"HP-Cap_{num_capitulo}.txt", "w", encoding="utf-8") as arquivo_capitulo:
                        arquivo_capitulo.write("---\n")
                        if tipo=="positivos":
                            arquivo_capitulo.write(f"positive:\n")
                        else:
                            arquivo_capitulo.write(f"negative:\n")
                        for palavra, quantidade in palavras_capitulo.items():
                            arquivo_capitulo.write(f"{palavra} - {quantidade}\n")
                        arquivo_capitulo.write(texto_original)

            busca_palavras("negativos")
            busca_palavras("positivos")
"""

