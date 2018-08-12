import flask, os
from flask import render_template, Flask

app = flask.Flask(__name__)

@app.route('/')
def home():
	return flask.render_template('home.html')

@app.route('/page2')
def page2():
    return flask.render_template('secondpage.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
