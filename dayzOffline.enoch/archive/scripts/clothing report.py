import xml.etree.ElementTree as ET
from collections import defaultdict

file = r"C:\Users\user\Documents\Github\7dayz\dayzOffline.enoch-1.29\db\types.xml"

tree = ET.parse(file)
root = tree.getroot()

data = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
tier_totals = defaultdict(int)
tier_usage_totals = defaultdict(lambda: defaultdict(int))

for t in root.findall("type"):
    cat = t.find("category")
    if cat is None or cat.attrib.get("name") != "clothes":
        continue

    nominal_el = t.find("nominal")
    nominal = int(nominal_el.text) if nominal_el is not None else 0
    if nominal == 0:
        continue

    tiers = [v.attrib.get("name", "Unknown") for v in t.findall("value")]
    usages = [u.attrib.get("name", "Unknown") for u in t.findall("usage")]
    name = t.attrib.get("name", "Unknown")

    if not tiers:
        tiers = ["Unknown"]
    if not usages:
        usages = ["Unknown"]

    for tier in tiers:
        tier_totals[tier] += nominal
        for usage in usages:
            tier_usage_totals[tier][usage] += nominal
            data[tier][usage][name] += nominal

for tier in sorted(data.keys()):
    print("=" * 50)
    print(f"  {tier}  —  total nominal: {tier_totals[tier]}")
    print("=" * 50)

    for usage in sorted(data[tier].keys()):
        print(f"\n  [{usage}]  —  nominal: {tier_usage_totals[tier][usage]}")
        for item, nominal in sorted(data[tier][usage].items()):
            print(f"    {item:<40} {nominal}")

    print()