import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for e in root.findall('country'):
    print(e.find('rank').text)
    print(e.get('name'))
    print(e.find('year').text)