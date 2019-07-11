SQLALCHEMY_DATABASE_URI = 'sqlite:////home/miroslav/Source/blog/instance/blog.db'
FLASK_ADMIN_SWITCH = 'cerulean'
FLATPAGES_ROOT = '/home/miroslav/Source/blog/articles/'
FLATPAGES_AUTO_RELOAD = 'DEBUG'
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code']
FLATPAGES_EXTENSION_CONFIGS = {
    'codehilite': {
        # 'linenums': True,
    }
}
POSTS_PER_PAGE = 10
