from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import LoginManager
import dash
import sqlite3
import os


# Create a login manager object
login_manager = LoginManager()

#instantiate dash app
app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

# comfig the server to interact with the database
# for production set secretkey as environmental variable
basedir = os.path.abspath(os.path.dirname(__file__))
server.config.update(
    SECRET_KEY='mysecretkey',
    SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(basedir, 'data.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(server)

# connect to existing db or create 
conn = sqlite3.connect(os.path.join(basedir, 'data.sqlite'))
engine = create_engine('sqlite:///'+ os.path.join(basedir, 'data.sqlite'))


login_manager.init_app(server)

# Tell users what view to go to when they need to login.
login_manager.login_view = "/login"