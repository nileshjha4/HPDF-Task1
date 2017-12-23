from flask import Flask, render_template
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
    return render_template('authors.html', data = data, count = count)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)