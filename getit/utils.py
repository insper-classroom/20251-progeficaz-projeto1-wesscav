import json

def load_data(filename):
    
    filepath = f"static/data/{filename}"
    
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def load_template(filename):

    filepath = f'static/templates/{filename}'

    with open(filepath, 'r', encoding="utf-8") as file:
        return file.read()
    
