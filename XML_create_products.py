import xml.etree.ElementTree as ET

root = ET.Element('shop')
category = ET.SubElement(root, 'category')
product_0 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
product_1 = ET.SubElement(category, 'product',{'name': 'Spaghetti Veganietto'} )

class Helper:
    def __init__(self, root, subeli):
        self.root = root
        self.subeli = subeli

    def add_subeli(self):
        for key in self.subeli:
            print(key)
            subeli = ET.SubElement(self.root, key)
            print(self.subeli[key])
            subeli.text= self.subeli[key]

Ob_0 = Helper(
                product_0,
                {'type': 'cereals',
                'producer': 'OpenEDG Testing Service',
                'price': '9.90',
                'currency': 'USD'}
               )

Ob_0.add_subeli()

Ob_1 = Helper(
                product_1,
                {'type': 'pasta',
                'producer': 'Programmers Eat Pasta',
                'price': '15.49',
                'currency': 'EUR'}
               )

Ob_1.add_subeli()

ET.dump(root)
tree = ET.ElementTree(root)
tree.write('lab.xml', 'UTF-8', True)
