from blog import db


class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    intro = db.Column(db.String(50))
    date_published = db.Column(db.DateTime)
    content = db.Column(db.Text)
