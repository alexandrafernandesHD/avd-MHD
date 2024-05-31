import os

diretorio = "D:\\Users\\lfher\\Dani\\UMinho\\Processamento de Linguagem  Prof João\\UMDicas_Limpos"

for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith(".md"):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        conteudo_novo = conteudo.replace('?**', '?**\n')
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo_novo)

print("Concluído!")
