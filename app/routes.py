from flask import render_template, flash, redirect
from app import site
from app.forms import LoginForm

@site.route('/')
@site.route('/index')
def index():
    user = {'username': "Miguel"}
    posts = [
        {
            'author': {'username': "John"},
            'body': "Beautiful day in Portland!",
            'date': "12/16/2017"
        },
        {
            'author': {'username': "Susan"},
            'body': "The Avengers movie was so cool!",
            'date': "08/21/2015"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    #return render_template('index.html', user=user)

@site.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
