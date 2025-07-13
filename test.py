import os
import json

folder = ".qode"
if not os.path.exists(folder):
    os.makedirs(folder)
    with open(f"{folder}/config.json", "w") as f:
        json.dump({"initialized": True}, f)
    print("Initialized custom tracker in .qode/")
else:
    print(".qode already exists.")
