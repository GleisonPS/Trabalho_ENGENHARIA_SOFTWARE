from flask import Flask, render_template, request, redirect, url_for, Blueprint
import sqlite3

product_service = Blueprint('product_service', __name__, template_folder='templates')

@product_service.route('/')
def index():
    
    return "Página product_service"
