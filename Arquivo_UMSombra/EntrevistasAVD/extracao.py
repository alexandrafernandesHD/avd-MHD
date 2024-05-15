import re

#o texto do meetgeek chegou aaté mim separado por tempos, este código guarda num texto novo apenas o texto corrido
# ou seja, chegou assim: 1 00:00:00,202 --> 00:00:03,263

def extrair_texto(transcricao):
    #encontrar o texto entre os tempos, 00:00:00,202 --> 00:00:03,263
    padrao = r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n(.+?)(?=\n\d+:\d+:\d+,\d+ -->|\Z)'
    texto_extraido = re.findall(padrao, transcricao, re.DOTALL)
    return '\n'.join(texto_extraido)

#ler o arquivo de transcrição
with open("captions.srt.txt", "r", encoding="utf-8") as file:
    transcricao = file.read()

#extrair o texto da transcrição
texto_extraido = extrair_texto(transcricao)

#remover o "1" em "1 00:00:00,202 --> 00:00:03,263"
texto_sem_numeros = re.sub(r'\n\d+\n', '\n', texto_extraido)

#resultado num novo arquivo chamado texto_extraido
with open("texto_extraido.txt", "w", encoding="utf-8") as file:
    file.write(texto_sem_numeros)

