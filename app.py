import flask

app = flask.Flask(__name__)

#renders index.html at route "/"
@app.route("/")
def hello(): 
	return flask.render_template("index.html")


if __name__== "__main__": 
	app.run()