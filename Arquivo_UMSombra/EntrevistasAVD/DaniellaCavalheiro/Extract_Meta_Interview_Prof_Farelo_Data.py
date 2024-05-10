import os
import re

def extract_metadata(content):
    metadata = {
        'interviewer': extract_interviewer(content),
        'interviewee': extract_interviewee(content),
        'date': extract_date(content),
        'title': 'Entrevista com Professor Mário Farelo',
        'type': 'Entrevista'
    }
    return metadata

def extract_interviewer(content):
    match_interviewer = re.search(r'<interviewer>(.*?)</interviewer>', content, re.IGNORECASE | re.DOTALL)
    if match_interviewer:
        return match_interviewer.group(1).strip()
    else:
        return None

def extract_interviewee(content):
    match_interviewee = re.search(r'<interviewee>(.*?)</interviewee>', content, re.IGNORECASE | re.DOTALL)
    if match_interviewee:
        return match_interviewee.group(1).strip()
    else:
        return None

def extract_date(content):
    match_date = re.search(r'<date>(.*?)</date>', content, re.IGNORECASE | re.DOTALL)
    if match_date:
        return match_date.group(1).strip()
    else:
        return None

def extract_interview_content(content):
    match_interview = re.search(r'<interview>(.*?)</interview>', content, re.IGNORECASE | re.DOTALL)
    if match_interview:
        return match_interview.group(1).strip()
    else:
        return None

def label_entities(content):
    # Etiquetar pessoas, lugares, organizações, etc.
    # Adicione mais etiquetas conforme necessário
    content = re.sub(r'(Universidade do Minho)', r'<organization>\1</organization>', content)
    content = re.sub(r'(Lab2PT)', r'<organization>\1</organization>', content)
    content = re.sub(r'(Arquivo Distrital de Braga)', r'<organization>\1</organization>', content)
    content = re.sub(r'(Universidade de Coimbra)', r'<organization>\1</organization>', content)
    content = re.sub(r'\b(Lisboa)\b', r'<place>\1</place>', content)  # Etiqueta Lisboa como local
    content = re.sub(r'\b(Évora|Algarve)\b', r'<place>\1</place>', content)  # Etiqueta Évora e Algarve como local
    # Adicione mais etiquetas para outros locais conforme necessário

    # Adicionando tags para entrevistador e entrevistado
    content = re.sub(r'entrevistador(a)?\s', r'<interviewer>\g<0></interviewer>', content)
    content = re.sub(r'entrevistado(a)?\s', r'<interviewee>\g<0></interviewee>', content)

    # Adicionando tags para perguntas e respostas
    content = re.sub(r'(?<=\n)(.*?\?)', r'<question>\1</question>', content)
    content = re.sub(r'(?<=\n)(.*?\.)(?=\n|$)', r'<answer>\1</answer>', content)

    return content

def save_metadata_and_content_to_md(metadata, interview_content, filename):
    md_content = "---\n"
    for key, value in metadata.items():
        md_content += f"{key.capitalize()}: {value}\n"
    md_content += "---\n\n"
    
    md_content += "<interview>\n"
    md_content += f"<interviewer>{metadata['interviewer']}</interviewer>\n"
    md_content += f"<interviewee>{metadata['interviewee']}</interviewee>\n"
    md_content += interview_content
    md_content += "\n</interview>"
    
    md_content = label_entities(md_content)
    
    md_filename = os.path.join(r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\Entrevista Prof Mario Farelo\Code", filename)
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

def main():
    caminho_arquivo_especifico = r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\Entrevista Prof Mario Farelo\Transcrições\Entrevista_Professor_Mario_Farelo_por_Daniella_Monteiro_Cavalheiro_Editado.txt"

    try:
        with open(caminho_arquivo_especifico, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            metadata = extract_metadata(conteudo)
            interview_content = extract_interview_content(conteudo)
            if interview_content:
                save_metadata_and_content_to_md(metadata, interview_content, "Entrevista_Professor_Mario_Farelo_Metadata.md")
    except Exception as e:
        print(f"Erro ao processar o arquivo {caminho_arquivo_especifico}: {str(e)}")

    print("Processo concluído para o arquivo Entrevista_Professor_Mario_Farelo_Metadata.md.")

if __name__ == "__main__":
    main()
