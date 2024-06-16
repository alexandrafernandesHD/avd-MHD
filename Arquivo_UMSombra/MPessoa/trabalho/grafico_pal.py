import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# Caminho correto do arquivo Excel no seu sistema local
excel_path = "C:/Users/dania/Downloads/trabalho/pals_ent_2.xlsx"
output_image_path = "C:/Users/dania/Downloads/trabalho/grafico_palavras.png"
output_excel_path = "C:/Users/dania/Downloads/trabalho/grafico_palavras_com_grafico.xlsx"

# Carregar o arquivo Excel
df = pd.read_excel(excel_path)

# Verificar as colunas do DataFrame
print("Colunas do DataFrame:", df.columns)

# Certificar-se de que os nomes das colunas estão corretos
df.columns = df.columns.str.strip()

# Ordenar os dados pela contagem de palavras
df = df.sort_values(by="Palavras", ascending=True)

# Criar o gráfico de barras horizontais
plt.figure(figsize=(10, 6))
plt.barh(df["Entrevista"], df["Palavras"], color='skyblue')
plt.xlabel('Número de Palavras')
plt.ylabel('Entrevista')
plt.title('Contagem de Palavras por Entrevista')
plt.grid(axis='x')

# Salvar o gráfico como imagem
plt.savefig(output_image_path)
print(f"Gráfico salvo como imagem em: {output_image_path}")

# Carregar o arquivo Excel novamente para adicionar o gráfico
wb = load_workbook(excel_path)
ws = wb.active

# Adicionar a imagem do gráfico ao Excel
img = Image(output_image_path)
ws.add_image(img, "E5")
print("Imagem do gráfico adicionada ao Excel.")

# Salvar o arquivo Excel com o gráfico
wb.save(output_excel_path)
print(f"Arquivo Excel com gráfico salvo em: {output_excel_path}")











