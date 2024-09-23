from flask import Flask, jsonify, request,Blueprint
import sqlite3

user_service = Blueprint("user_service",__name__)

def init_db():
    # Função para inicializar o banco de dados e criar a tabela 'users' se não existir
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    conn.commit()
    conn.close()

@user_service.route('/', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return jsonify(users) # Retorna os usuários em formato JSON

@user_service.route('/', methods=['POST'])
def add_user():
    # Obtém os dados do novo usuário da requisição JSON
    novo_user = request.get_json()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name, email) VALUES (?, ?)', (novo_user['name'], novo_user['email']))
    conn.commit()
    conn.close()
    return jsonify(novo_user), 201 # Retorna os dados do novo usuário em formato JSON e status 201 (Criado)


