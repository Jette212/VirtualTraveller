from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("main.html")

@app.route("/weather/<location>")
def weather(location):
	return "sunny!"

app.run(debug=True)