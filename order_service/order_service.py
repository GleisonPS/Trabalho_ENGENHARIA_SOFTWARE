from flask import Flask, render_template, request, redirect, url_for, Blueprint
import sqlite3

order_service = Blueprint('order_service', __name__, template_folder='templates')

@order_service.route('/')
def index():
    
    return "Página order_service"
