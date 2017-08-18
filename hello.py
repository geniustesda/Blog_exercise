# coding:utf-8
from flask import Flask 
from flask import request	
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	return "<h1> Hello World! </h1>"

@app.route('/<name>')
def welcome(name):
    return "<h1>Hello %s !</h1>" %name

@app.route('/ua')
def Ua():
	user_agent = request.headers.get("User-Agent")
	return "<p>Your brwoser is: '%s'</p>" % user_agent

if __name__ == "__main__":
    manager.run()