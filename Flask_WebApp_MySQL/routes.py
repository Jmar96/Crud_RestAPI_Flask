from flask import Blueprint, render_template

main = Blueprint('main', __name__) #routename = main

@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')