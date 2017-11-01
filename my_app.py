from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("main.html")

app.run(debug=True)
