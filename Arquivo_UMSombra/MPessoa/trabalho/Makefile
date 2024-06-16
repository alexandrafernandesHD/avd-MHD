corpus-umsombra.txt: extrai-body.py
	python extrai-body.py

metadados.txt: extrai_metadados.py 
	python extrai_metadados.py

corpus-anotado.txt: anota.py corpus-umsombra.txt
	python anota.py corpus-umsombra.txt

verbos.txt: contaverbos.py corpus-anotado.txt
	python contaverbos.py corpus-anotado.txt

nomes.txt: contanomes.py corpus-anotado.txt
	python contanomes.py corpus-anotado.txt

adjetivos.txt: contadjetivos.py corpus-anotado.txt
	python contadjetivos.py corpus-anotado.txt

propn.txt: contapropn.py corpus-anotado.txt
	python contapropn.py corpus-anotado.txt

loc.txt: contaloc.py corpus-anotado.txt
	python contaloc.py corpus-anotado.txt

person.txt: contaper.py corpus-anotado.txt
	python contaper.py corpus-anotado.txt

org.txt: contaorg.py corpus-anotado.txt
	python contaorg.py corpus-anotado.txt

lemas.txt: contalemas.py corpus-anotado.txt
	python contalemas.py corpus-anotado.txt

pals_ent.txt: contapals.py corpus-umsombra.txt
	python contapals.py corpus-umsombra.txt

