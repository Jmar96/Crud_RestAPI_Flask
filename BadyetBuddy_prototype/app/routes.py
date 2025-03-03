from flask import Blueprint, jsonify, render_template
from .models import Badyet_Items
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/items', methods=['GET'])
def get_items():
    b_items = Badyet_Items.query.all()
    return jsonify([
        {
            'id': item.id, 
            'name': item.name, 
            'description': item.description, 
            'category': item.category, 
            'length': item.length, 
            'amount': item.amount
        } for item in b_items
    ])
