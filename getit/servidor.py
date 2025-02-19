from flask import Flask, render_template_string, request, redirect, flash
import sqlite3 as sql
from utils import load_data, load_template, save_data
import views

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())
#quando a rota é /, a função de cima é chamada e chama a função views.index() que lê o arquivo
#notes.html e mostra as notes desejadas e gera a lista notes que vai ser utilizada no index.html


@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')

    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("INSERT INTO notes (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    con.commit() 
    con.close()  

    return redirect('/')

@app.route("/edit_user/<int:id>", methods=['POST', 'GET'])
def edit_user(id):
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    if request.method == 'POST':
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']

        cur.execute("UPDATE notes SET titulo=?, detalhes=? WHERE id=?", (titulo, detalhes, id))
        con.commit()
        return redirect('/')

    cur.execute("SELECT * FROM notes WHERE id=?", (id,))
    data = cur.fetchone()
    con.close()

    return redirect('/')

@app.route("/delete_user/<int:id>", methods=['GET'])
def delete_user(id):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("DELETE FROM notes WHERE id=?", (id,))
    con.commit()
    con.close()
    
    # Redirecionar para a página inicial após a exclusão
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
