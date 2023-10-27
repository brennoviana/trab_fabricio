from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '03cc225e97c901944b70d44f3b077cab8e3553923d89b409'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://brenno:B15182225*@localhost/empresa'

db = SQLAlchemy(app)