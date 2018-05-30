from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app

posts = [
    {
        'author': 'redwan',
        'title': 'Post 1',
        'content': 'first post',
        'date_posted': 'May 14, 2018'
    },
    {
        'author': 'younes',
        'title': 'Post 2',
        'content': 'first post ffsad',
        'date_posted': 'May 10, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Registeration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'me@aa.com' and form.password.data == 'password':
            flash(f'You have logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Username or Password is incorrect', 'danger')
    return render_template('login.html', title='login', form=form)
