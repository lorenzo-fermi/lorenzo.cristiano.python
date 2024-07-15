import xml.etree.ElementTree as ET

#documento XMl come stringa 

xml_data = '''<prodotti>
<prodotto>
<nome>Laptop</nome>
<prezzo>800</prezzo>
</prodotto>
<prodotto>
<nome>Smartphone</nome>
<prezzo>500</prezzo>
</prodotto>
<prodotto>
<nome>Tablet</nome>
<prezzo>300</prezzo>
</prodotto>
</prodotti>'''

#analizza il documento xml 
root = ET.fromstring(xml_data)

#cerca e stampa i prodotti con un prezzo inferiore a 600 
for prodotto in root.findall("prodotto"):
    nome = prodotto.find("nome").text
    prezzo = int(prodotto.find("prezzo").text)
    if prezzo < 600: 
        print(f"Nome: {nome}, Prezzo: {prezzo}")