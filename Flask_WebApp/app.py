from flask import Flask


def create_app():
    app = Flask(__name__)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run('127.0.0.1', 5000)