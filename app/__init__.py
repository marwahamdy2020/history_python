# import flask and import modules/extensions
from flask import Flask
from dotenv import load_dotenv
import config
#from app.models import db
import os


# ceate app object
app = Flask(__name__)

# Environment configrations
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get['ENV'])

# data base
# db.create_all()
# db.session.commit()
