from flask import Flask
from flask_restful import Api
 
app = Flask(__name__)
 
api = Api(app) #Flask REST Api code 
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000)