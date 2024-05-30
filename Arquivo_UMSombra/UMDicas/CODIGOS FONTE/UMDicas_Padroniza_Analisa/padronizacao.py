import os
from grava_arquivo import grava_resultado

def padronizacao():
    diretorio = "Arquivos"
    cabecalhos_originais=[]
    #Lista para abrigar os cabeçalhos originais dos arquivos de entrada
    cabecalhos_corretos=["university","journal","issue","date","title","topic","interviewee","role","interviewer"]
    #Lista para abrigar os cabeçalhos padronizados que serão postos nos arquivos de saída
    def coleta_cabecalhos(diretorio): #Faz a coleta dos cabeçalhos originais
        for filename in os.listdir(diretorio):
            print(filename)
            if filename.endswith('.md'): # Verifica se o arquivo é um arquivo Markdown
                filepath = os.path.join(diretorio, filename)
                with open(filepath, 'r', encoding="utf-8") as file:
                    lines = file.read()
                    partes=lines.split("---") 
                    #ESTE CABEÇALHO TERÁ A LISTA DE ARQUIVOS E DE TAGS DOS ARQUIVOS
                    cabecalhos_originais.append([filename,partes[1], partes[2]])
        
        return cabecalhos_originais
    
    coleta_cabecalhos(diretorio)

    for item in cabecalhos_originais: #Padroniza os cabeçalhos originais e os adiciona aos novos arquivos com o corpo do texto logo em seguida, separados por "---" conforme o padrão definido em aula
        if len(item) == 3:
            if item[0][10]==".":
                i=10
            else:
                i=11
            novo_filename=f"{item[0][:i]}-Entrevista{item[0][-4]}.md"
            print(novo_filename)
            grava_resultado(f"---\n",novo_filename,"a","Arquivos/Novos_Arquivos")#Cria o novo arquivo em "Novos_Arquivos"
            meta_individual=item[1].splitlines()
            metas_arquivo=[]
            for meta in meta_individual:
                if len(meta)>0:
                    valores=meta.split(":")
                    tag=valores[0]
                    if len(valores)>1:
                        valor_tag=valores[1]
                    else:
                        valor_tag="valor em branco"
                    grava_resultado(f"\{item[0]}|{tag}|{valor_tag}\n","tags2.txt","a","Tags")
                    metas_arquivo.append([tag,valor_tag])
                else:
                    grava_resultado(f"\{item[0]},linha em branco, linha em branco\n","tags2.md","a","Tags")#Grava os metadados também em um arquivo "Tags/Tags2.md"
            for cabecalho in cabecalhos_corretos:
                for meta in metas_arquivo:
                    if cabecalho == meta[0]:
                        tag=meta[0]
                        valor_tag=meta[1]
                        grava_resultado(f"{tag}: {valor_tag}\n",novo_filename,"a","Arquivos/Novos_Arquivos")#Grava o arquivo com o cabeçalho padronizado em "Novos_Arquivos"
                        grava_resultado(f"\{novo_filename}|{tag}|{valor_tag}\n","tags_Novas_2.txt","a","Tags")#Grava os metadados também em um arquivo "Tags/Tags2.txt"
                    else:
                        if meta[0] in cabecalho:
                            tag=cabecalho
                            valor_tag=None
                            grava_resultado(f"{tag}: {valor_tag}\n",novo_filename,"a","Arquivos/Novos_Arquivos")
            grava_resultado(f"---\n",novo_filename,"a","Arquivos/Novos_Arquivos")
            #Hora de remover quebras de linhas no meio das frases e marcar as perguntas das entrevistas em negrito...
            texto_original=item[2].splitlines()
            texto_ajustado=""
            for i, linha in enumerate(texto_original,0):
                if i==0:
                    texto_ajustado=linha
                else:
                    if len(linha)>0 and linha[-1] in ['?', '!', '.','”'] or len(linha)==0:
                        texto_ajustado=texto_ajustado+f" {linha}\n\n"
                    else:
                        texto_ajustado=texto_ajustado+f" {linha}"
            texto_marcado=texto_ajustado.splitlines()
            for linha in texto_marcado: #Grava as linhas de texto formatado em seus espectivos arquivos dentro de "Novos_Arquivos"
                if len(linha)>2:
                    if linha[-1]=="?":
                        grava_resultado(f"**{linha}**\n\n",novo_filename,"a","Arquivos/Novos_Arquivos")
                    else:
                        grava_resultado(f"{linha}\n\n",novo_filename,"a","Arquivos/Novos_Arquivos")