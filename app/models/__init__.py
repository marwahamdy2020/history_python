from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create data base
db = SQLAlchemy(app)

# data base
db.create_all()
# db.session.commit()
