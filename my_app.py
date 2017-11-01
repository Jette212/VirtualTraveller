app = Flask("MyApp")

@app.route("/")
def hello():
	return "Hello World"

app.run(debug=True)
