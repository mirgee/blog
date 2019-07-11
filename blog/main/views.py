from blog import db, posts, app
from blog.main.models import Blogpost
from flask import redirect, render_template, request, url_for, Blueprint
from datetime import datetime
from flask_flatpages import pygments_style_defs
import readtime


main = Blueprint('main', __name__, template_folder='templates',
                 static_folder='static')


@main.route('/')
def index():
    def validate(date_text):
        try:
            datetime.strptime(date_text, '%d-%m-%Y')
            return True
        except (ValueError, TypeError):
            return False

    published_posts = (p for p in posts if 'date' in p.meta and
                       validate(p.meta['date']))
    latest = sorted(published_posts, reverse=True,
                    key=lambda p: p.meta['date'])

    for post in latest:
        setattr(post, 'readtime', str(readtime.of_markdown(post.body)))
        setattr(post, 'num_comments', 0)

    ppp = app.config['POSTS_PER_PAGE']
    max_pages = len(latest) // ppp
    page = max(0,
               min(max_pages, request.args.get('page', 0, type=int)))
    print(f'page={page}')

    prev_url = url_for('main.index', page=page-1) if page > 0 else None
    next_url = \
        url_for('main.index', page=page+1) if page+1 <= max_pages else None

    return render_template('index.html', posts=latest[page*ppp:(page+1)*ppp],
                           prev_url=prev_url, next_url=next_url)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/posts/<path:path>')
def post(path):
    post = posts.get_or_404(path)
    return render_template('post.html', post=post)


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/add')
def add():
    return render_template('add.html')


@main.route('/addpost', methods=['POST'])
def addpost():
    print(request.form)
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author,
                    content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


@main.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}
