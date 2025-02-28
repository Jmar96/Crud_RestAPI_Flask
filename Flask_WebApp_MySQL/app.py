from flask import Flask, render_template
from config import Config
from extensions import db
from flask_migrate import Migrate
from routes import main 


def create_app():
    # create instance and pass the special variable __name__ as an argument, which helps Flask determine the root path for the application.
    app = Flask(__name__)
    # load configuration setting
    app.config.from_object(Config)
    # calls the function and passes the app object (your Flask application instance) to it.
    register_resources(app)
    # call the function for migration
    register_extension(app)

    return app

def register_extension(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_resources(app):
    app.register_blueprint(main)
    # I stopped here because it's not working or running anymore -> https://www.youtube.com/watch?v=L6f5i8aL1gU&list=PLXpWu84ZnHT-e-f6d_r6Q21cTsGAS4xXX&index=3

if __name__ == "__main__":
    app = create_app()
    app.run('127.0.0.1', 5000)