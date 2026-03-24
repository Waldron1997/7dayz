import xml.etree.ElementTree as ET

red_deer_file = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\env\red_deer_territories.xml"
roe_deer_file = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\env\roe_deer_territories.xml"
reindeer_file = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\env\reindeer_territories.xml"

reindeer_output = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\env\reindeer_territories.xml"
red_deer_output = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\env\red_deer_territories.xml"
roe_deer_output = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\env\roe_deer_territories.xml"

TIER3_MAX_Z = 3500

def any_zone_below(territory):
    return any(float(z.attrib.get("z", 0)) < TIER3_MAX_Z for z in territory.findall("zone"))

# Red and roe deer — remove any territory that has a zone below 3500
for filepath, output_path, label in [
    (red_deer_file, red_deer_output, "Red Deer"),
    (roe_deer_file, roe_deer_output, "Roe Deer"),
]:
    tree = ET.parse(filepath)
    root = tree.getroot()
    before = len(root.findall("territory"))
    for t in root.findall("territory"):
        if any_zone_below(t):
            root.remove(t)
    after = len(root.findall("territory"))
    print(f"{label}: {before} -> {after} territories ({before - after} removed)")
    ET.indent(ET.ElementTree(root), space="    ")
    ET.ElementTree(root).write(output_path, encoding="UTF-8", xml_declaration=True)

# Reindeer — keep only territories that have a zone below 3500
tree = ET.parse(reindeer_file)
root = tree.getroot()
before = len(root.findall("territory"))
for t in root.findall("territory"):
    if not any_zone_below(t):
        root.remove(t)
after = len(root.findall("territory"))
print(f"Reindeer: {before} -> {after} territories ({before - after} removed)")
ET.indent(ET.ElementTree(root), space="    ")
ET.ElementTree(root).write(reindeer_output, encoding="UTF-8", xml_declaration=True)


