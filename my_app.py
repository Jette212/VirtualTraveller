from flask import Flask, render_template

app = Flask("MyApp")

def what_is_weather(location):
	import requests
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": location, "units":"metric", "appid":"3b503bfa7ea64695d425e95faf892625"}
	response = requests.get(endpoint, params=payload)
	return response.json()["weather"][0]["description"] + '<br/>' + str(response.json()["main"]["temp"]) + '<br/>' + str(response.json()["main"]["temp_min"]) + '<br/>' + str(response.json()["main"]["temp_max"])   

@app.route("/")
def hello():
	return render_template("main.html")

@app.route("/weather/<location>")
def weather(location):
	return str(what_is_weather(location))


#API for exchange rates
#20580abfe5aa991c3c0c67bf5b6c3f25

#API for news: 80fb8990d33c49128aab4e2a2990583b

app.run(debug=True)