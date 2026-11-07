import json 

class StorageService:
    def __init__(self, path="data/project_data.json"):
        self.path = path

    def load(self):
        with open(self.path, "r") as file:
            return json.load(file)

    def save(self, data):
        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)