from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.secret_key = 'chave'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://brenno:B15182225*@localhost/empresa'

db = SQLAlchemy(app)