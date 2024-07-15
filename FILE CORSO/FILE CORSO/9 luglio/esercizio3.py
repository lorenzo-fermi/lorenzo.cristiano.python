import xml.etree.ElementTree as ET

# Documento XML iniziale
xml_data = '''<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>'''
 

#analisi del documento xml 
root = ET.fromstring(xml_data)

#creazione del nuovo elemento libro
new_book=ET.Element("libro")
titolo=ET.SubElement(new_book, "titolo")
titolo.text="learning python"
autore=ET.SubElement(new_book,"autore")
autore.text="mark lutz"

#aggiunta del nuovo libro alla radice 
root.append(new_book)

#creazione dell'oggetto elementree
tree=ET.ElementTree(root)

#stampa del documento xml
ET.dump(root)

#salvataggio del documneto xml modificato su file 
tree.write('libri_modificato.xml', encoding='utf-8', xml_declaration=True)