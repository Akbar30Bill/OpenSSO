from flask import Flask, request
from db import *
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/signup/user', methods=['POST'])
def SignUpUser():
    data = request.json
    username, password = data['username'], data['password']
    result = create_user(username, password)
    return result

@app.route('/signup/service', methods=['POST'])
def SignUpService():
    data = request.json
    name, username, password = data['name'], data['username'], data['password']
    result = create_service(name, username, password)
    return result
