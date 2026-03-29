import xml.etree.ElementTree as ET

file = r"C:\Users\twaldron\Github\7dayz\dayzOffline.enoch\db\types.xml"

tree = ET.parse(file)
root = tree.getroot()

matching_types = []

for t in root.findall("type"):
    name = t.attrib.get("name", "")
    
    # Check for <category name="clothes"/>
    is_clothes = any(
        cat.attrib.get("name") == "clothes"
        for cat in t.findall("category")
    )
    
    # Check for <nominal>0</nominal>
    nominal_el = t.find("nominal")
    is_zero_nominal = nominal_el is not None and nominal_el.text == "0"
    
    if is_clothes and is_zero_nominal:
        matching_types.append(name)

print(f"Types with category='clothes' and nominal=0 ({len(matching_types)} found):")
for name in sorted(matching_types):
    print(name)