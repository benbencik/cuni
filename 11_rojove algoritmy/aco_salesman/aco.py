import xml.etree.ElementTree as ET
import sys
import os

test = "data_32.xml"
# test = "data_72.xml"
# test = "data_422.xml"
tree = ET.parse(f"data/{test}")
root = tree.getroot()

cat = {"info": 0, "network": 1, "fleet": 2, "requests": 3}  # categories
# n_attr = {"nodes": 0, "euclidean": 1, "decimals": 2}  # network_attributes

# fleet info
for child in root[1]:
    for ch in child:
        # print(ch.tag, ch.attrib)
        print(ch.attrib["id"])
        print(ch[0].text)

# load graph

