from app import app
from flask_sqlalchemy import SQLAlchemy

# create data base
db = SQLAlchemy(app)
