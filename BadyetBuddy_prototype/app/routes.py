from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from .models import Badyet_Items
from . import db
from .util import query_helper

import sqlite3

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
    return jsonify(query_helper.get_all_items())

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
    a_total = query_helper.get_sum("income")

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
    b_total = query_helper.get_sum("expense")

    return render_template('dashboard.html', incomes=incomes, expenses=expenses, incm_total=a_total, expn_total=b_total, page="dashb")

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

@main.route('/add', methods=["POST"])
def add_record():
    name = request.form.get("name")
    description = request.form.get("description")
    category = request.form.get("category")
    length = request.form.get("length")
    amount = request.form.get("amount")
    owner_id = request.form.get("owner_id")
    
    pg_name = request.form.get("pg_name")

    if name and description and category and length and amount and owner_id:
        new_record = Badyet_Items(name=name, description=description, category=category, length=length, amount=float(amount), owner_id=owner_id)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for(f"main.{pg_name}"))
    return "Failed to add record. Ensure all fields are filled in."


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_record(id):
    record = Badyet_Items.query.get_or_404(id)
    if request.method == "POST":
        record.name = request.form.get("name")
        record.description = request.form.get("description")
        record.category = request.form.get("category")
        record.length = request.form.get("length")
        record.amount = request.form.get("amount")

        db.session.commit()
        return redirect(url_for("main.dashboard"))
    return render_template("edit.html", record=record)