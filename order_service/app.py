from flask import Flask, jsonify, request,Blueprint
import sqlite3
import requests

order_service = Blueprint("order_service",__name__)

def init_db():
    # Função para inicializar o banco de dados e criar a tabela 'orders' se não existir
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS orders (
              id INTEGER PRIMARY KEY, 
              user_id INTEGER, 
              product_id INTEGER,
              qtd INTEGER,
              preco REAL)'''
              )
    conn.commit()
    conn.close()

@order_service.route('/', methods=['POST'])
def create_order():
    order_data = request.get_json()
    
    # Valida o ID do usuário
    user_response = requests.get(f'http://localhost:5001/users/{order_data["user_id"]}')
    if user_response.status_code != 200:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    # Valida o ID do produto
    product_response = requests.get(f'http://localhost:5002/products/{order_data["product_id"]}')
    if product_response.status_code != 200:
        return jsonify({"error": "Produto não encontrado"}), 404
    
    # Conexão com o banco de dados de pedidos
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    
    # Insere o pedido no banco de dados
    c.execute('INSERT INTO orders (user_id, product_id) VALUES (?, ?)', 
              (order_data['user_id'], order_data['product_id']))
    conn.commit()
    
    # Recupera o ID do pedido inserido
    order_id = c.lastrowid
    
    conn.close()
    
    # Cria o pedido para retorno
    order = {
        "id": order_id,
        "user_id": order_data['user_id'],
        "product_id": order_data['product_id']
    }
    
    return jsonify(order), 201  # Retorna o pedido criado e status 201

@order_service.route('/', methods=['GET'])
def get_orders():
    # Conexão com o banco de dados de pedidos
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('SELECT * FROM orders')
    orders = c.fetchall()
    conn.close()
    
    # Converte o resultado para uma lista de dicionários
    orders_list = [{"id": order[0], "user_id": order[1], "product_id": order[2]} for order in orders]
    
    return jsonify(orders_list)

'''if __name__ == '__main__':
    init_db()
    app.run(port=5003)  # Executa a aplicação Flask na porta 5003
'''