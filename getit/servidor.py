from flask import Flask, render_template_string, request, redirect, flash, render_template
import sqlite3 as sql
from utils import load_data, load_template, save_data, load_template_with_data
import views

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(views.index())

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

@app.route("/edit_note/<int:uid>", methods=['POST', 'GET'])
def edit_note(uid):
    if request.method == 'GET':
        return render_template_string(views.edit_note(uid))
    else:
        views.edit_note(uid)
        return redirect('/')

@app.route("/delete_note/<int:uid>", methods=['GET'])
def delete_note(uid):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("DELETE FROM notes WHERE uid=?", (uid,))
    con.commit()
    con.close()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)