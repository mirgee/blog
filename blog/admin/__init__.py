from blog import admin, db
from blog.main.models import Blogpost
from flask_admin.contrib.sqla import ModelView

__all__ = ['views']

admin.add_view(ModelView(Blogpost, db.session))
