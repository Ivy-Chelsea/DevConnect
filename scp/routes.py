from flask import render_template, url_for, redirect
from scp import app
from flask_login import current_user


@app.route("/")
def landing():
    return render_template('landing.html', title='landing page')


app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))


app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
