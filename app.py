"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index/')
def index():
    return 'Index page'
    
@app.route('/user/<username>/')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/authors/')
def getAuthorsCount():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    count = [0] * (len(data)+1)
    for i in posts:
       count[i['userId']] += 1
    authors = '<b>Hello! Below is the list containing name of authors and a count of thier posts</b><br><br><br>'
    for i in data:
        authors += '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<b><i>' + i['name'] + '</i></b> has published <b>' + str(count[i['id']]) + '</b> articles' '<br><br>'
    return authors

if __name__ == '__main__':
    app.run()