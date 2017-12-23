from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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