from flask import Flask, render_template, request, redirect, url_for, Blueprint
import sqlite3

user_service = Blueprint('user_service', __name__, template_folder='templates')

@user_service.route('/')
def index():
    db = sqlite3.connect("user_service.sql")
    
    return "Página user_service"
