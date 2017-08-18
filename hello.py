# coding:utf-8
from flask import Flask 
from flask import request	
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/user/<name>')
def welcome(name):
    return render_template ("user.html", name=name)

@app.route('/ua/user-agent')
def Ua():
	user_agent = request.headers.get("User-Agent")
	return ("<p>Your brwoser is: '%s'</p>" % user_agent)

if __name__ == "__main__":
    manager.run()