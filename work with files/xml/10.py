import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('shop.xml')
root = tree.getroot()

# Extract and display product details
for product in root.findall('product'):
    id = product.find('id').text
    name = product.find('name').text
    price = product.find('price').text
    description = product.find('description').text
    
    print(f"Product ID: {id}")
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Description: {description}")
    print()
