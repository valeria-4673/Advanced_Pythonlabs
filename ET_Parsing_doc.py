import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('nyse.xml')
acciones = tree.getroot()

print("COMPANY"+"\t"*3+"LAST"+"\t"*3+"CHANGE"+"\t"*3+"MIN"+"\t"*3+"MAX")
for quote in acciones:
    name= quote.text
    atributos = quote.attrib
    last= atributos['last']
    change= atributos['change']
    mini= atributos['min']
    maxi= atributos['max']
    print(name.ljust(30), last.ljust(30))
