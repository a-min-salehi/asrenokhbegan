import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('shop.xml')
root = tree.getroot()

# Extract and display product details
for product in root.findall('product'):
    price = product.find('price')
    if int(price.text) > 500 :
        price.set('class', 'expensive')
    else:
        price.text = str(int(price.text) + 0.03* int(price.text))

tree.write('output.xml')
print("Modified XML file successfully.") 

       
