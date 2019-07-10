from blog import db
from sqlalchemy.sql import func


class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    intro = db.Column(db.String(50))
    date_published = db.Column(db.DateTime(timezone=True), default=func.now())
    content = db.Column(db.Text)
