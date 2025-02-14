from flask import Flask, render_template_string, request, redirect
from utils import load_data, load_template
import views

app = Flask(__name__)

NOTE_TEMPLATE = '''  <li>
    <h3>{title}</h3>
    <p>{details}</p>
  </li>
'''

RESPONSE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="{{{{ url_for('static', filename='img/logo-getit.png') }}}}">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
{s}
</ul>

</body>
</html>
'''

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    notes_li = [
        load_template('components/note.html').format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    response = load_template('index.html').format(notes=notes)

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    #apos receber as informações e submetê-las, é redirecionado para a home
    views.submit(titulo, detalhes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)