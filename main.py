from flask import Flask, render_template, request, redirect, url_for
from order_service.app import order_service
from product_service.app import product_service
from user_service.app import user_service

import sqlite3

app = Flask(__name__)


app.register_blueprint(order_service, url_prefix='/order_service')
app.register_blueprint(product_service,url_prefix='/product_service')
app.register_blueprint(user_service, url_prefix='/user_service')

if __name__=="__main__":
    app.run(debug=True)