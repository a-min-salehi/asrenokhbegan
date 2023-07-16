import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('library.xml')

# Get the root element of the XML
root = tree.getroot()

# Access and work with the XML data
for child in root:
    print(child.tag, child.attrib)

# Find elements with a specific tag
elements = root.findall('book')
for element in elements:
    print(element.find('title').text)
