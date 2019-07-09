from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

from blog.main.views import Blogpost
from blog.admin.views import ModelView

# admin = Admin(app, name='blog', template_mode='bootstrap')
admin = Admin(app)
admin.add_view(ModelView(Blogpost, db.session))
