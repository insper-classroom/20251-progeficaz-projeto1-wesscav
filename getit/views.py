from utils import load_data, load_template
import utils
import json
import sqlite3 as sql

def index():
    # Conectar ao banco de dados SQLite
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row  # Retorno como dicionário
    cur = con.cursor()
    
    # Buscar todas as notas da tabela "notes"
    cur.execute("SELECT titulo, detalhes, uid FROM notes")
    notes_data = cur.fetchall()
    con.close()  # Fechar a conexão

    # Gerar o HTML das notas
    note_template = load_template('components/notes.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'], uid=dados['uid'])
        for dados in notes_data
    ]
    notes = '\n'.join(notes_li)
    return load_template('index.html').format(notes=notes)
    


def submit(titulo, detalhes):
    # Conectar ao banco de dados SQLite
    con = sql.connect("db_web.db")
    cur = con.cursor()
    
    # Inserir a nova nota no banco de dados
    cur.execute("INSERT INTO notes (titulo, detalhes, uid) VALUES (?, ?, ?)", (titulo, detalhes, uid))
    con.commit()  # Salvar alterações
    con.close()  # Fechar a conexão

