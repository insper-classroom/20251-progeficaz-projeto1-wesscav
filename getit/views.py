from utils import load_data, load_template
import utils
import json

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    #adiciona uma nova anotação ao arquivo notes.json,

    notes = load_data('notes.json')
    notes.append({'titulo': titulo, 'detalhes': detalhes})
    
    with open('static/data/notes.json', 'w') as file:
        json.dump(notes, file, indent=4)