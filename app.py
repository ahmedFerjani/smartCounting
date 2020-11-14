from flask import Flask, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# enable cors
CORS(app)

# import configuration
app.config.from_pyfile('config/config.cfg')

app.debug = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

from resources.routes import initialize_routes

initialize_routes(Api(app))

