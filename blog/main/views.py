from blog import app, db, posts
from blog.main.models import Blogpost
from flask import redirect, render_template, request, url_for
from datetime import datetime
import readtime


@app.route('/')
def index():
    # List all files in the articles folder, order by date_published, trim to
    # few (only public ones)
    # Create intro automatically from the first few hundred characters,
    # estimate time_to_read based on length
    # id, img_uri, date_published, time_to_read, intro, num_comments
    # posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    published_posts = (p for p in posts if 'date_published' in p.meta)
    latest = sorted(published_posts, reverse=True,
                    key=lambda p: p.meta['date_published'])
    for post in latest:
        setattr(post, 'readtime', str(readtime.of_markdown(post)))
        setattr(post, 'num_comments', 0)
    return render_template(url_for('main', 'index.html'), posts=latest[:10])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<path:path>')
def post(path):
    # post = Blogpost.query.filter_by(id=post_id).one()
    post = posts.get_or_404(path)
    return render_template('post.html', post=post)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addpost', methods=['POST'])
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
