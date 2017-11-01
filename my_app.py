from flask import Flask, render_template

app = Flask("MyApp")

def what_is_weather(location):
	import requests
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": location, "units":"metric", "appid":"3b503bfa7ea64695d425e95faf892625"}
	response = requests.get(endpoint, params=payload)
	return response.json()["weather"][0]["description"] + '<br/>' + str(response.json()["main"]["temp"])


@app.route("/")
def hello():
	return render_template("main.html")

@app.route("/weather/<location>")
def weather(location):
	return str(what_is_weather(location))

app.run(debug=True)