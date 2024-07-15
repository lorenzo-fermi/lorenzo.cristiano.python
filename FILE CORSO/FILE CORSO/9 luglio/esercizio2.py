import xml.etree.ElementTree as ET 

#elenco studenti 

studenti = [
    {'nome': 'Alice', 'eta': '22'},
    {'nome': 'Bob', 'eta': '25'},
    {'nome': 'Charlie', 'eta': '20'}
]

#creazione dell'elemento della radice 

root=ET.Element("studenti")

#aggiunta degli studenti all'elemento della radice 
for studente in studenti:
    studente_element= ET.SubElement(root, "studente")
    nome_element= ET.SubElement(studente_element, "nome")
    nome_element.text= studente["nome"]
    eta_element=ET.SubElement(studente_element, "eta")
    eta_element.text=studente["eta"]

#creazione dell'oggetto elementetree

tree=ET.ElementTree(root)

#salvataggio del documento XMl su file 

tree.write("studenti.xml", encoding="utf-8", xml_declaration=True)

#output di conferma 

print("Documento XMl creato e salvato come 'studenti.xml'")