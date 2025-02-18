import json

def load_data(filename):
    
    filepath = f"static/data/{filename}"
    
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def load_template(filename):

    filepath = f'static/templates/{filename}'

    with open(filepath, 'r', encoding="utf-8") as file:
        return file.read()
    

    # filepath = f"static/data/{filename}"
    
    # #connect to SQLite
    # con = sqlite3.connect(filepath)
    
    # #Create a Connection
    # cur = con.cursor()
    
    # #Drop users table if already exsist.
    # data = cursor.fetchall()
    
    # # Fecha a conexão
    # conn.close()