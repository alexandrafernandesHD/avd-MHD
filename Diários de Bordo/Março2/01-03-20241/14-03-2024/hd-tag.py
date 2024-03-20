# pip install -U spacy
# python -m spacy download pt_core_news_lg
# en_core_web_sm
import spacy

# Load Portuguese tokenizer, tagger, parser and NER
nlp = spacy.load("pt_core_news_lg")

# Process whole documents
text = ("""Bom dia, Alvaro Álvaro Iriarte da Silva. Onde onde é que nasceu? Em em Viana do Castelo.""")
doc = nlp(text)

# Analyze Syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

for fr in doc.sents:
    print (f"====={fr.text}" )
    for pal in doc:    #para todas as palavras no doc vou escrever alguma coisa acerca delas
        print(f"{pal.text}\t{pal.pos_}\t{pal.lemma_}\t{pal.morph}\t{pal.rank}")
        # f"{pal.text}\tpos={pal.pos_}\tlema={pal.lemma_}\tmorf={pal.morph} {pal.rank}")
