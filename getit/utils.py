import json

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

    # filepath = f"static/data/{filename}"
    
    # #connect to SQLite
    # con = sqlite3.connect(filepath)
    
    # #Create a Connection
    # cur = con.cursor()
    
    # #Drop users table if already exsist.
    # data = cursor.fetchall()
    
    # # Fecha a conexão
    # conn.close()