from flask import Flask, render_template, request, make_response, send_file
import requests

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello, Nilesh!'

@app.route('/authors/')
def getAuthorsCount():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    count = [0] * (len(data)+1)
    for i in posts:
       count[i['userId']] += 1
    return render_template('authors.html', data = data, count = count)

@app.route('/setcookie/', methods=['GET','POST'])
def setCookie():
    if request.method == 'POST' :
        resp = make_response("Cookies set sucessfully")
        resp.set_cookie('name', request.form.get('name') )
        resp.set_cookie('age', request.form.get('age') )
        return resp
    return render_template('setcookie.html')

@app.route('/getcookie/')
def getCookie():
    return render_template('getcookie.html', name=request.cookies.get('name'), age=request.cookies.get('age') )

@app.route('/robot.txt/')
def deny():
    return render_template('deny.html'), 404

@app.route('/image/')
def image():
    return send_file('media\\homer-simpson.jpg')

@app.route('/input/', methods=['GET','POST'])
def input():
    if request.method=='POST':
        print(request.form.get('text'))
        return 'POST Data log to stdout sucessfully! Please check terminal.'
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)