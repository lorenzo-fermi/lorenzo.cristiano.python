import xml.etree.ElementTree as ET

# Definizione del documento XML
xml_data = '''<studenti>
<studente>
<nome>Alice</nome>
<eta>22</eta>
</studente>
<studente>
<nome>Bob</nome>
<eta>25</eta>
</studente>
</studenti>'''

# Analisi del documento XML
root = ET.fromstring(xml_data)

# Stampa dei nomi e delle età degli studenti
for studente in root.findall('studente'):
    nome = studente.find('nome').text
    eta = studente.find('eta').text
    print(f'Nome: {nome}, Età: {eta}')

# Salvataggio del documento XML su file
tree = ET.ElementTree(root)
with open("studenti.xml", "wb") as files:
    tree.write(files)


