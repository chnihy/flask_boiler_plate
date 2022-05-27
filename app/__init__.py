from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.debug = True

# initialize bootstrap
bootstrap = Bootstrap(app)

from app import routes
