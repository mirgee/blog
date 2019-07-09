from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

admin = Admin(app, name='blog', template_mode='bootstrap')

import blog.main.views
import blog.admin.views
