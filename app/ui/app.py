# Required Imports
from flask import Flask, render_template, request
import requests

import contextlib
import os
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = os.environ.get("SECRET_KEY")

# ensure the instance folder exists
with contextlib.suppress(OSError):
    os.makedirs(app.instance_path)

@app.route('/', methods=('GET', 'POST'))
def index():
    #GET REQUEST - gets data
    response = requests.get("http://api:8000/users")
    users = response.json()
    name= request.args.get('name')
    email = request.args.get('email')
    verified = False
    #POST REQUEST - sends data
    if name and email:
        data = {'name':name, 'email':email}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post("http://api:8000/verify", data=json.dumps(data), headers=headers)
        results = response.json()
        app.logger.debug(f'VERIFIED: {results}')
        verified = results.get('results')
    return render_template("index.html", users=users, verified = verified)


# if __name__ == "__main__":
#     app.run(
#         host=app.config['HOST'],
#         port=app.config['PORT'],
#     )