import xml.etree.ElementTree as ET
import math
import functools
import numpy as np
import namedtouple



# test = "data_32.xml"
# test = "data_72.xml"
test = "data_422.xml"
tree = ET.parse(f"aco_salesman/data/{test}")
root = tree.getroot()

cat = {"info": 0, "network": 1, "fleet": 2, "requests": 3}  # categories
Vertex = namedtuple('Vertex', ['name', 'x', 'y'])
Request = namedtuple('Request', ['name', 'destination', 'size'])

# fleet info
capacity = -1
for fleet in root[cat["fleet"]]: cap = fleet[2].text

# graph
warehouse = -1
vertices = []
for nodes in root[cat["network"]]:
    for node in nodes:
        if node.attrib["id"] == "0": warehouse = int(node.attrib["id"])
        vertices.append(Vertex(int(node.attrib['id']), float(node[0].text), float(node[1].text)))

# requests
requests = []
for req in root[cat["requests"]]:
    print(req.attrib)
    requests.append(Request(int(req.attrib["id"]), int(req.attrib["node"]), float(req[0].text)))



# fitness bude dĺžka ktorú som prešiel a ešte tam treba dať penalizáciu za počet áut
# ako sa to bude vykreslovat


# --------------------------------------------------------------------------------------------------------

@functools.lru_cache(maxsize=None)
def distance(v1, v2):
    return math.sqrt((v1.x - v2.x)**2+(v1.y - v2.y)**2)