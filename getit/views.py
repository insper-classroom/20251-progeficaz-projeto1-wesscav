from utils import load_data, load_template
import utils
import json
import sqlite3 as sql
from flask import request, redirect

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

def edit_note(uid):
    # Conectar ao banco de dados SQLite
    con = sql.connect("db_web.db")
    cur = con.cursor()
    
    # Buscar todas as notas da tabela "notes"
    cur.execute("SELECT titulo, detalhes FROM notes where uid=?", (uid,))
    note_especifica = cur.fetchone()
    print(note_especifica[1])


    # Gerar o HTML das notas
    note_template = load_template('edit_note.html')
    # notes_li = [
    #     note_template.format(title=dados['titulo'], details=dados['detalhes'], uid=uid)
    #     for dados in note_especifica
    # ]
    # notes = '\n'.join(notes_li)
    

    if request.method == 'POST':
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']
        uid = uid
        cur.execute("UPDATE notes SET titulo=?, detalhes=? WHERE uid=?", (titulo, detalhes, uid))
        con.commit()
        con.close()
        return

    con.close()  # Fechar a conexão
    return load_template('edit_note.html').format(title=note_especifica[0], details=note_especifica[1], uid=uid)
    # .format(title=dados[''])
    