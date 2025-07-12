import os
import json

folder = ".mytracker"
if not os.path.exists(folder):
    os.makedirs(folder)
    with open(f"{folder}/config.json", "w") as f:
        json.dump({"initialized": True}, f)
    print("Initialized custom tracker in .mytracker/")
else:
    print(".mytracker already exists.")
