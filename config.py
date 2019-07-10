from flask import render_template_string
from flask_flatpages.utils import pygmented_markdown


def my_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)


SQLALCHEMY_DATABASE_URI = 'sqlite:////home/miroslav/Source/blog/instance/blog.db'
FLASK_ADMIN_SWITCH = 'cerulean'
FLATPAGES_ROOT = '/home/miroslav/Source/blog/articles/'
FLATPAGES_AUTO_RELOAD = 'DEBUG'
FLATPAGES_EXTENSION = '.md'
FLATPAGES_EXTENSION_CONFIG = {
    'codehilite': {
        'linenums': 'True'
    }
}
FLATPAGES_HTML_RENDERER = my_renderer
