import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\UM_Dicas_Codes\interviewees_gender.csv"
data = pd.read_csv(file_path)

# Exibir as primeiras linhas do DataFrame para inspeção
data.head()

# Contar o número total de entrevistas
total_interviews = data.shape[0]

# Criar o gráfico de barras para o número total de entrevistas
plt.figure(figsize=(8, 6))
plt.bar(['Total Interviews'], [total_interviews], color='skyblue')
plt.ylabel('Number of Interviews')
plt.title('Total Number of Interviews')
plt.show()
