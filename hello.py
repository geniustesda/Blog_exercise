# coding:utf-8
from flask import Flask 
from flask import request	
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
	return render_template("index.html", current_time=datetime.utcnow())

@app.route('/user/<name>')
def welcome(name):
    return render_template ("user.html", name=name)

@app.route('/user-agent')
def Ua():
	user_agent = request.headers.get("User-Agent")
	return render_template("user-agent.html", user_agent=user_agent, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template("500.html"),500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")