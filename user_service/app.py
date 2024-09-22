from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def init_db():
    # Função para inicializar o banco de dados e criar a tabela 'users' se não existir
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    conn.commit()
    conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return jsonify(users) # Retorna os usuários em formato JSON

@app.route('/users', methods=['POST'])
def add_user():
    # Obtém os dados do novo usuário da requisição JSON
    novo_user = request.get_json()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name, email) VALUES (?, ?)', (novo_user['name'], novo_user['email']))
    conn.commit()
    conn.close()
    return jsonify(novo_user), 201 # Retorna os dados do novo usuário em formato JSON e status 201 (Criado)

if __name__ == '__main__':
    init_db()
    app.run(port=5001) # Executa a aplicação Flask na porta 5001

