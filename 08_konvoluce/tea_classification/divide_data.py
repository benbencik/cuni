import os
import random
import shutil

classes = ["gyokuro", "matcha", "maté", "pu-erh", "shoumei"]
test_nb = 5
train_nb = 25
cwd = os.getcwd()

# creating new directories
try:
    shutil.rmtree("test_data")
    shutil.rmtree("train_data")
except FileNotFoundError:
    print("creating new dirs...")

os.makedirs(os.path.join(cwd, "test_data"))
os.makedirs(os.path.join(cwd, "train_data"))

for c in classes: os.makedirs(os.path.join(cwd, f"test_data/{c}"))
for c in classes: os.makedirs(os.path.join(cwd, f"train_data/{c}"))


# divide the images into train and test directories
for c in classes:
    test_images = random.sample(range(1, 31), test_nb)
    print(test_images)
    for num in range(1, 31):
        if num in test_images:
            shutil.copyfile(os.path.join(cwd, f"dataset_resized/{c}/{num}.jpg"), 
                            os.path.join(cwd, f"test_data/{c}/{num}.jpg"))
        else:
            shutil.copyfile(os.path.join(cwd, f"dataset_resized/{c}/{num}.jpg"), 
                            os.path.join(cwd, f"train_data/{c}/{num}.jpg"))