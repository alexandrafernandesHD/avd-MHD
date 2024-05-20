#!/usr/bin/env python3

from jjcli import * 
import yaml

docs = glob("Nos/*.md") #um glob que apanha uma lista de ficheiros
print(f"Nos: {len(docs)}")
cl = clfilter("")
cl.args = sorted(docs) 

for txt in cl.text():
    # print(txt[:100])
    for metadados in re.findall(r'---(.*)---', txt, flags=re.S): #o ponto não apanha new lines, por isso o re.S 
        #print (metadados)
        #print ("----------")
        dicmeta = yaml.safe_load(metadados)
        print (f"{dicmeta.get('date')}::{dicmeta.get('title')} :: {cl.filename()}")