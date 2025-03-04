from flask import Blueprint, jsonify, render_template
from .models import Badyet_Items
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', page="home")

@main.route('/about')
def about():
    return render_template('about.html', page="about")

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
            'amount': item.amount,
            'owner_id': item.owner_id
        } for item in b_items
    ])

@main.route('/dashboard')
def dashboard():
    a_items = Badyet_Items.query.filter_by(category='income').all()
    incomes = [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'length': item.length,
            'amount': item.amount,
            'owner_id': item.owner_id
        } for item in a_items
    ]

    b_items = Badyet_Items.query.filter_by(category='expense').all()
    expenses = [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'length': item.length,
            'amount': item.amount,
            'owner_id': item.owner_id
        } for item in b_items
    ]
    return render_template('dashboard.html', incomes=incomes, page="dashb")

@main.route('/incomes')
def incomes():
    b_items = Badyet_Items.query.filter_by(category='income').all()
    incomes = [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'length': item.length,
            'amount': item.amount,
            'owner_id': item.owner_id
        } for item in b_items
    ]
    return render_template('incomes.html', incomes=incomes)

@main.route('/expenses')
def expenses():
    b_items = Badyet_Items.query.filter_by(category='expense').all()
    expenses = [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'length': item.length,
            'amount': item.amount,
            'owner_id': item.owner_id
        } for item in b_items
    ]
    return render_template('expenses.html', expenses=expenses)
