import xml.etree.ElementTree as ET
import sys
import os

test = "data_32.xml"
# test = "data_72.xml"
# test = "data_422.xml"
tree = ET.parse(f"data/{test}")
root = tree.getroot()
cat = {"info": 0, "network": 1, "fleet": 2, "requests": 3}  # categories

# fleet info
cap = -1
for fleet in root[cat["fleet"]]: cap = fleet[2].text

# graph
warehouse = -1
graph = {}
for nodes in root[cat["network"]]:
    for node in nodes:
        if node.attrib["id"] == "0": warehouse = int(node.attrib["id"])
        graph[int(node.attrib["id"])] = {"x": node[0].text, "y": node[1].text}

# requests
req = {}
for request in root[cat["requests"]]:
    req[int(request.attrib["id"])] = {"dest": int(request.attrib["node"]), "size": float(request[0].text)}
