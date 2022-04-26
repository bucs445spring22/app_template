import contextlib
from models.user import User
# Required Imports
import os
import pytest
from flask import Flask, request

app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.config.from_object('config.Config')
# ensure the instance folder exists

with contextlib.suppress(OSError):
    os.makedirs(app.instance_path)

@app.route('/users', methods=('GET',))
def index():
    return User.all()

@app.route('/verify', methods=('POST',))
def verify():
    print(f'FORM: {request.json}')
    name = request.json.get('name')
    email = request.json.get('email')
    u = User(name, email)
    return u.verify()

@app.route('/tests', methods=('GET',))
def tests():
    retcode = pytest.main(["-x", "tests"])
