from flask import Flask, render_template_string, request, redirect
from utils import load_data, load_template
import views

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

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

