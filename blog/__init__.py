from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from flask_admin import Admin
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('instance.config')

db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

posts = FlatPages(app)

from blog.main.views import Blogpost, main
from blog.admin.views import ModelView

app.register_blueprint(main)

# admin = Admin(app, name='blog', template_mode='bootstrap')
admin = Admin(app)
admin.add_view(ModelView(Blogpost, db.session))
