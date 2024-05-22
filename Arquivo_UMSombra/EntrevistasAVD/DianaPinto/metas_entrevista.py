caminho_arquivo_txt = "entrevista_avd.txt"
caminho_arquivo_md = "entrevista_avd.md"

with open(caminho_arquivo_txt, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()


linhas_md = []
for linha in linhas:
  
    linhas_md.append(linha.rstrip() + "  \n")
    
with open(caminho_arquivo_md, 'w', encoding='utf-8') as arquivo_md:
    arquivo_md.writelines(linhas_md)

print(f"Arquivo Markdown '{caminho_arquivo_md}' criado com sucesso!")