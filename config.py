# Config Code

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_session import Session
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather-station-database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)

Session(app)


