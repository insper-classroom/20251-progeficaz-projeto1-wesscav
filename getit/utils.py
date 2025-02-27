import json
from flask import render_template

def load_data(filename):
    
    filepath = f"static/data/{filename}"
    
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def load_template(filename):

    filepath = f'static/templates/{filename}'

    with open(filepath, 'r', encoding="utf-8") as file:
        return file.read()
    
def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_template_with_data(filename, data):
    
    filepath = "static/templates/edit_note.html"

    titulo = data['titulo']
    detalhes = data['detalhes']
    uid = data['uid']

    return render_template(filepath).format(title=titulo, details=detalhes, uid=uid)
