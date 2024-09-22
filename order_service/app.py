from flask import Flask, render_template, request, redirect, url_for, Blueprint
import sqlite3

order_service = Blueprint('order_service', __name__, template_folder='templates')

@order_service.route('/')
def index():
    db = sqlite3.connect("order_Service.sql")
    
    return "Página order_service"
