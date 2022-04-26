import os
import random
import shutil

classes = ["gyokuro", "matcha", "maté", "pu-erh", "shoumei"]
cwd = os.getcwd()

# shutil.rmtree("test_data")
# shutil.rmtree("train_data")
os.makedirs(os.path.join(cwd, "test_data"))
os.makedirs(os.path.join(cwd, "train_data"))

for c in classes: os.makedirs(os.path.join(cwd, f"test_data/{c}"))
for c in classes: os.makedirs(os.path.join(cwd, f"train_data/{c}"))

