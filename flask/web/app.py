from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import os

app = Flask(__name__)

db_user = os.environ['POSTGRES_USER']
db_pwd = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']
db_host = os.environ['POSTGRES_HOST']
db_port = '5432'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s/%s' % (db_user, db_pwd, db_host, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(128))
    author = db.Column(db.String(32))
    date_posted = db.Column(db.DateTime)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        text = request.form['text']
        author = request.form['author']
        blog_post = Post(text=text, author=author, date_posted=datetime.now())
        db.session.add(blog_post)
        db.session.commit()
        posts = Post.query.order_by(desc(Post.date_posted))
        return render_template('index.html', posts=posts)

    posts = Post.query.order_by(desc(Post.date_posted))
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
