from flask import render_template
from app import site

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

    #return render_template('index.html', user=user)
    return render_template('index.html', title='Home', user=user, posts=posts)
