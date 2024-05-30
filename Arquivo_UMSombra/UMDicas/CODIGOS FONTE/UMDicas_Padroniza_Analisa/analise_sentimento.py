import os
from grava_arquivo import*
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import spacy
from textblob import download_corpora
from textblob import TextBlob


def analise_sentimento():

    nlp = spacy.load("pt_core_news_sm") #python -m spacy download pt_core_news_sm
    nltk.download('punkt')
    nltk.download('vader_lexicon')
    # download_corpora()

    dicionario_palavras = {}
    dicionario_palavras_totais={}

    diretorio = "Arquivos/Novos_Arquivos"
    textos_entrevistas=[]
    #Lista para abrigar os textos das entrevistas para análise de sentimentos
    def coleta_textos_entrevistas(diretorio): #Faz a coleta dos cabeçalhos originais
        for filename in os.listdir(diretorio):
            print(filename)
            if filename.endswith('.md'): # Verifica se o arquivo é um arquivo Markdown
                filepath = os.path.join(diretorio, filename)
                with open(filepath, 'r', encoding="utf-8") as file:
                    lines = file.read()
                    partes=lines.split("---")
                    #Guarda o nome o arquivo, o cabeçalho com os metas e o texto da entrevista separadamente
                    textos_entrevistas.append([filename,partes[1], partes[2]])
        return textos_entrevistas
    
    coleta_textos_entrevistas(diretorio)

    def analisa(texto):
        sia = SentimentIntensityAnalyzer()
        texto_tokenizado=nltk.sent_tokenize(texto)
        for palavra in texto_tokenizado:
            score_sentimento = sia.polarity_scores(palavra)
            print(f"\n-----------\nFrase:{palavra}\nScore Sentimento:{score_sentimento['compound']}")
        return score_sentimento['compound']

    for entrevista in textos_entrevistas: #Início do processamento do texto de cada entrevista, individualmente
        if len(entrevista) == 3:
            novo_filename=f"{entrevista[0][:-3]}-Analise.md"
            print(novo_filename)
            grava_resultado(f"#ANALISE DE SENTIMENTOS\n\n",novo_filename,"a","Arquivos/Novos_Arquivos/Analise")#Cria o novo arquivo de Análise em "Novos_Arquivos"
            meta_individual=entrevista[1].splitlines()
            for meta in meta_individual:
                grava_resultado(f"- {meta}\n",novo_filename,"a","Arquivos/Novos_Arquivos/Analise")
            grava_resultado(f"## Análise por Frase\n\n",novo_filename,"a","Arquivos/Novos_Arquivos/Analise")
            texto_individual=entrevista[2].splitlines()
            for linha in texto_individual:
                dicionario_palavras.clear()#limpa o dicionario de palavras de cada texto individual, processado anteriormente
                if not linha[1:2]=="*" and len(linha)>2 and not linha[:1]=="#":
                    score_texto=analisa(linha)
                    grava_resultado(f"{linha}|{score_texto}\n",novo_filename,"a","Arquivos/Novos_Arquivos/Analise")
                    palavras_linha=linha.split()
                    for palavra in palavras_linha:
                        score_palavra=analisa(palavra)
                        #Adiciona no dicionario de palavras do isolado
                        if palavra not in dicionario_palavras:
                            dicionario_palavras[palavra] = {"palavra": palavra, "score": score_palavra, "contagem": 1}
                        else:
                            dicionario_palavras[palavra]["contagem"] += 1
                        #Adiciona no dicionario de palavras totais de todos os textos
                        if palavra not in dicionario_palavras_totais:
                            dicionario_palavras_totais[palavra] = {"palavra": palavra, "score": score_palavra, "contagem": 1}
                        else:
                            dicionario_palavras_totais[palavra]["contagem"] += 1          
            grava_resultado(f"## Análise por Palavra\n\n",novo_filename,"a","Arquivos/Novos_Arquivos/Analise")
            for palavra in dicionario_palavras.values():
                grava_resultado(f"{palavra['palavra']}|{palavra['score']}|{palavra['contagem']}\n",novo_filename,"a","Arquivos/Novos_Arquivos/Analise")
            blob = TextBlob(entrevista[2])
            sentimento_total = 0.0
            for sentenca in blob.sentences:
                sentimento = sentenca.sentiment.polarity
                print(f"Sentença: {sentenca}\nSentimento: {sentimento}")
                sentimento_total += sentimento
            print(f"\nSentimento Total: {sentimento_total}")
            grava_resultado(f"{novo_filename}|{sentimento_total}\n","Sentimentos_Totais.md","a","Arquivos/Novos_Arquivos/Analise")









    for palavra in dicionario_palavras_totais.values():
        grava_resultado(f"{palavra['palavra']}|{palavra['score']}|{palavra['contagem']}\n","Palavras_Totais.md","a","Arquivos/Novos_Arquivos/Analise")