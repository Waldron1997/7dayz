import xml.etree.ElementTree as ET

file_a = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.chernarusplus\db\types.xml"
file_b = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch\db\types.xml"

tree_a = ET.parse(file_a)
tree_b = ET.parse(file_b)

root_a = tree_a.getroot()
root_b = tree_b.getroot()

types_a = {t.attrib["name"]: t for t in root_a.findall("type")}
types_b = {t.attrib["name"]: t for t in root_b.findall("type")}

missing_in_b = types_a.keys() - types_b.keys()

print("Missing types:")
for name in sorted(missing_in_b):
    print(name)


