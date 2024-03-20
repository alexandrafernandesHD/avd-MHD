from jjcli import * 

from bs4 import BeautifulSoup as bs 


ats = glob("1095-1101/Article.aspx*") #Função glob para obter uma lista de arquivos que têm nomes começando com "Article.aspx" no diretório "ext"
print(ats)

fo = open("saida1.txt", "w", encoding = "utf-8")  #Abre um arquivo chamado "saida.txt" no modo de escrita ("w") 

def proc_article(html): #Define uma função chamada proc_article que recebe uma string HTML como argumento.
    #print(len(html))  #está a contar os caracteres de cada artigo
    a=bs(html)  #cria uma árvore
    cabecalho = "" 
    for meta in a.find_all("meta"):
        p = meta.get("property") #Itera sobre todas as tags "meta" no HTML, extrai o atributo "property"
        if p is None:
            continue 
        p = p.replace("og:", "") #se existir, remove o prefixo "og:"
        cabecalho+= f"{p}: {meta.get('content')}\n" #constrói uma string chamada cabecalho com o nome da propriedade e seu conteúdo.
        #print(p, ":" , meta.get("content"))
    art = a.find("div", id="artigo")
    print("==========\n", cabecalho, art.get_text(), file = fo)
    


for file in ats: #Itera sobre a lista de arquivos obtida anteriormente. Para cada arquivo, lê o conteúdo HTML, chama a função proc_article para processar o HTML e extrair informações relevantes, e imprime os resultados no arquivo de saída.
    with open (file, encoding="utf-8") as f:
        html = f.read()
    proc_article(html)







"""<meta property='og:title' content='A nova bengala robótica'/><meta property='og:url' content='http://www.nos.uminho.pt/Article.aspx?id=3686'/><meta property='og:image' content='http://www.nos.uminho.pt/Images/destaques/20231222192503_Bengala1a.jpg'/><meta property='og:site_name' content='Jornal Online UMINHO A nova bengala robótica'/><meta property='og:description' content='

'/><meta property='og:type' content='blog'/>

<div id="artigo">
                    <div class="title">
                        
                        <div class="voltar">


<h1>
                        <span id="ctl00_ContentPlaceHolder1_LabelTitle">A nova bengala robótica</span></h1>
                    <span class="creditos">
                        <span id="ctl00_ContentPlaceHolder1_LabelInfo">22-12-2023 | Beatriz Mendes | Fotos: BirdLab</span>
                    </span>


"""


