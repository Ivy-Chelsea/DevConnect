from flask import render_template, url_for, redirect
from scp import app, bcrypt
from flask_login import current_user
from scp.form import *
from scp.models import *


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
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()



app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
