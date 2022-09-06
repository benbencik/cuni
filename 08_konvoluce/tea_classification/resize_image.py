from PIL import Image
import os

classes = ["gyokuro", "matcha", "maté", "pu-erh", "shoumei"]
cwd = os.getcwd()
newsize = (224, 224)

for c in classes:
    for i in range(1, 31):
        im = Image.open(os.path.join(cwd, "dataset_resized", f"{c}/{i}.jpg"))
        im = im.resize(newsize)
        im.save(os.path.join(cwd, "dataset_resized", f"{c}/{i}.jpg"))