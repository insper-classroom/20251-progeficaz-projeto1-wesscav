import json

def load_data(filename):
    
    filepath = f"static/data/{filename}"
    
    with open(filepath, "r") as file:
        return json.load(file)
