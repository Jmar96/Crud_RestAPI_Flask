from flask import Blueprint, jsonify, request, abort,render_template
from .models import Badyet_Items
from . import db

import os


main = Blueprint('main', __name__)

@main.route('/')
def home():
    print("Current working directory:", os.getcwd())
    return render_template('index.html')


# GET ALL USERS - GET
@main.route('/items', methods=['GET'])
def get_users():
    b_items = Badyet_Items.query.all()
    return jsonify([
        {
            'id': u.id, 
            'name': u.name, 
            'description': u.description, 
            'category': u.category, 
            'length': u.length, 
            'amount': u.amount
        } for u in b_items
    ])