from flask import Flask, render_template_string
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_flatpages import FlatPages
from flask_sqlalchemy import SQLAlchemy
from markdown import markdown
from bs4 import BeautifulSoup


def my_renderer(text, posts):
    rendered_md = render_template_string(text)
    rendered_html = markdown(
        rendered_md,
        extensions=app.config['FLATPAGES_MARKDOWN_EXTENSIONS'],
        extension_configs=app.config['FLATPAGES_EXTENSION_CONFIGS'],
    )
    soup = BeautifulSoup(rendered_html, 'lxml')
    # TODO: cssutils may be a little better suited for this
    quotes = soup.find_all('blockquote')
    if quotes:
        for quote in quotes:
            quote['class'] = 'blockquote m-lg-5 py-3 pl-4 px-lg-5'
            footers = quote.find('footer')
            if footers:
                for footer in footers:
                    footer['class'] = 'blockquote-footer'
    tables = soup.find_all('table')
    if tables:
        for table in tables:
            table['class'] = 'table table-striped my-5'
    h3s = soup.find_all('h3')
    if h3s:
        for h3 in h3s:
            h3['class'] = 'mt-5 mb-3'
    h5s = soup.find_all('h5')
    if h5s:
        for h5 in h5s:
            h5['class'] = 'my-3'
    uls = soup.find_all('ul')
    if uls:
        for ul in uls:
            ul['class'] = 'mb-5'
    ols = soup.find_all('ol')
    if ols:
        for ol in ols:
            ol['class'] = 'mb-5'
    lis = soup.find_all('li')
    if lis:
        for li in lis:
            li['class'] = 'mb-2'
    return soup


app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('instance.config')
app.config.update({'FLATPAGES_HTML_RENDERER': my_renderer})

db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

posts = FlatPages(app)

from blog.admin.views import ModelView
from blog.main.views import Blogpost, main

app.register_blueprint(main)

# admin = Admin(app, name='blog', template_mode='bootstrap')
admin = Admin(app)
admin.add_view(ModelView(Blogpost, db.session))
