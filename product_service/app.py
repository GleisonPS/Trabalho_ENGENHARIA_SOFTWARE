from flask import Flask, jsonify, request,Blueprint
import sqlite3

product_service = Blueprint("product_service",__name__)

# Função para inicializar o banco de dados e criar a tabela 'products' se não existir
def init_db():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
    conn.commit()
    conn.close()

# Rota para obter todos os produtos
@product_service.route('/', methods=['GET'])
def get_products():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    products = c.fetchall()
    conn.close()
    return jsonify(products)  # Retorna os produtos em formato JSON

# Rota para adicionar um novo produto
@product_service.route('/', methods=['POST'])
def add_product():
    novo_produto = request.get_json()  # Obtém os dados do novo produto da requisição JSON
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('INSERT INTO products (name, price) VALUES (?, ?)', (novo_produto['name'], novo_produto['price']))
    conn.commit()
    conn.close()
    return jsonify(novo_produto), 201  # Retorna os dados do novo produto e status 201 (Criado)

