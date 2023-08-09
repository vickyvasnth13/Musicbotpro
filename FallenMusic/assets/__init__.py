import os

boobs = []

for pussy in os.listdir("AnonX/assets"):
    if pussy.endswith("png"):
        boobs.append(pussy[:-4])

