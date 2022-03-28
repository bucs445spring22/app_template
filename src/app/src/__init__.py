# Required Imports
import os

from flask import Flask, render_template
import sass

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.secret_key = os.environ.get("SECRET_KEY")
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.before_request
    def before_request_tasks():
        sass.compile(dirname=('static/style/sass', 'static/style'), output_style='nested')

    with app.app_context():
        # Include our Routes
        @app.route('/', methods=('GET', 'POST'))
        def index():
            return render_template("index.html")

    return app