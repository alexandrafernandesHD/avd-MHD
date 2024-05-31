## README do Projeto "UMDicas" - Extração e Tratamento de Dados

Este README detalha o projeto de extração e tratamento de dados do jornal UMDicas, uma publicação da Universidade do Minho, como parte do curso de Mestrado em Humanidades Digitais na Escola de Letras, Artes e Ciências Humanas - ELACH.

## Descrição do Projeto

O jornal UMDicas teve sua primeira publicação em abril de 2003 e é disponibilizado em formato impresso e PDF. Ele cobre temas relacionados à academia, cultura, desporto e ação social, oferecendo entrevistas, reportagens sobre eventos e anúncios da comunidade acadêmica. Todas as edições estão disponíveis para consulta online, exceto a primeira.

## Objetivo

O principal objetivo deste projeto é extrair e tratar o conteúdo das edições do jornal UMDicas utilizando técnicas de scraping, para posteriormente transferir os dados coletados para um corpus. Este corpus permitirá a visualização gráfica de pessoas, lugares e eventos, colaborando para contar a história da Universidade do Minho. Este trabalho será integrado com os projetos de outros grupos (NOS, ComUM, Museu da Pessoa).

## Estrutura do Projeto

### Etapas do Projeto

1. **Coleta de Dados**:
   - Utilização de técnicas de web scraping para extrair o conteúdo das edições do jornal disponíveis online.
   - Ferramentas utilizadas: BeautifulSoup e Scrapy.
   - Salvamento dos dados em formatos estruturados (TXT, MD, CSV, XML).

2. **Tratamento de Dados**:
   - Limpeza e pré-processamento dos dados coletados.
   - Extração de metadados relevantes (datas, entrevistados, entrevistadores, títulos, tópicos).
   - Uso de Python para scripts de tratamento de dados (pandas, spacy, NLTK).

3. **Análise e Visualização de Dados**:
   - Criação de visualizações gráficas para representar as informações extraídas.
   - Ferramentas de visualização: Matplotlib, Seaborn, Plotly.
   - Geração de gráficos e mapas para identificar tendências e padrões: Heatmap.

### Bibliotecas Utilizadas

Para extrair e processar as informações, utilizamos várias bibliotecas:

- **Regular Expressions (re)**: Manipulação de texto e extração de padrões específicos.
- **PIL (Pillow)**: Manipulação e processamento de imagens.
- **pytesseract**: Interface Python para o Tesseract OCR para reconhecimento de texto em imagens.
- **Fitz (PyMuPDF)**: Leitura, manipulação e extração de informações de documentos PDF.
- **Counter**: Contagem da frequência das palavras (parte da biblioteca collections).
- **BeautifulSoup**: Extração e manipulação de dados HTML.
- **nltk (Natural Language Toolkit)**: Limpeza de texto, remoção de stop words, e outras tarefas de processamento de linguagem natural.
- **sklearn**: Tarefas de machine learning e feature extraction.
- **Spacy**: Tokenização, lematização e reconhecimento de entidades.
- **Genderize**: Previsão de gênero com base nos nomes.
- **feature_extraction.text**: Parte da sklearn para extração de keywords e palavras frequentes não comuns.

### Desafios Enfrentados

A maior dificuldade foi aprimorar o código para o processamento do corpus e a comparação entre os jornais, identificando pontos em comum e criando gráficos legíveis. O processo exigiu múltiplas reescritas do código e um registro cuidadoso das experiências malsucedidas.

Além disso, lidar com a grande quantidade de informação desorganizada exigiu uma limpeza adicional do código para permitir uma filtragem mais eficiente do conteúdo, apresentando assim os maiores 'chunks' ao invés de uma lista enorme.

### Limpeza de Dados e Stop Words

Um passo crucial foi a limpeza dos dados, incluindo a remoção de stop words. Utilizamos a biblioteca nltk para remover palavras comuns que geralmente não agregam valor significativo à análise, como preposições, artigos e pronomes.

### Estrutura dos Códigos Utilizados

- `UMDicas_Scraping.py`: Script para realizar o scraping dos conteúdos do jornal.
  - Funções principais:
    - `fetch_editions()`: Coleta os links de todas as edições disponíveis.
    - `extract_content()`: Extrai o conteúdo de cada edição.
  - Manipulação de exceções para lidar com problemas de conexão e dados incompletos.

- `UMDicas_Data_Cleaning.py`: Script para limpeza e pré-processamento dos dados.
  - Funções principais:
    - `clean_text()`: Remove caracteres especiais e normaliza o texto.
    - `extract_metadata()`: Extrai informações como datas e autores dos artigos.
  - Uso de pandas para manipulação de DataFrames.

- `UMDicas_Visualization.py`: Script para criação de visualizações gráficas.
  - Funções principais:
    - `plot_timeline()`: Cria uma linha do tempo dos eventos mencionados nas edições.
    - `generate_wordcloud()`: Gera nuvens de palavras para visualizar as palavras mais frequentes.
  - Integração com Plotly para interatividade.

## Organização dos Arquivos

- **docs/**:
  - `UMDicas_Overview.pdf`: Documento com uma visão geral do projeto.
  - `UMDicas_Data_Schema.pdf`: Esquema dos dados extraídos e tratados.

- **data/**:
  - `raw/`: Dados brutos extraídos diretamente do scraping.
  - `cleaned/`: Dados limpos e pré-processados prontos para análise.

- **scripts/**:
  - `UMDicas_Scraping.py`
  - `UMDicas_Data_Cleaning.py`
  - `UMDicas_Visualization.py`

- **results/**:
  - `visualizations/`: Gráficos e mapas gerados.
  - `reports/`: Relatórios de análise de dados.


## Conclusão

O projeto foi uma oportunidade de aplicar e aprimorar nossos conhecimentos em processamento de linguagem natural e análise de texto. As dificuldades encontradas, especialmente na organização e limpeza dos dados, foram superadas com um trabalho cuidadoso e detalhado, resultando em uma análise mais precisa e eficiente dos jornais estudados.

## Colaboradores

- **Cristiana Gomes - PG52760**
- **Daniella Monteiro - PG54506**
- **Diana Pinto - PG54507**
- **Lívia Bettero - PG52762**

## Professores

- **Alvaro Iriarte Sanromán**
- **José João A. G. Dias de Almeida**

## Links Úteis

- [Site do Jornal UMDicas](https://www.sas.uminho.pt/noticias/jornal-umdicas)
- [Relatório Colab] (https://colab.research.google.com/drive/1w6UR06k5rBReySVqqhYhT4ShuJprow6m?usp=sharing)
- [Apresentação Gamma] (https://gamma.app/docs/UMDicas-117wvtn1ybze7w3?mode=doc)

## Atualizações

Mais informações e atualizações sobre o progresso do projeto serão adicionadas conforme necessário.

---

