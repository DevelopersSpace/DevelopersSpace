from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
	return render_template("Homepage.html")
@app.route("/Arduino")
def more():
	return render_template("Arduino.html")