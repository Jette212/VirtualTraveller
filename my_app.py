import json
import requests
from flask import Flask, render_template

app = Flask("MyApp")

def code_to_capital(code):
	endpoint = "https://restcountries.eu/rest/v2/alpha/" + code
	response = requests.get(endpoint)
	return response.json()["capital"]

def what_is_weather(location):
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": location, "units":"metric", "appid":"3b503bfa7ea64695d425e95faf892625"}
	response = requests.get(endpoint, params = payload)
	return response.json()["weather"][0]["description"] + '<br/>' + str(response.json()["main"]["temp"]) + '<br/>' + str(response.json()["main"]["temp_min"]) + '<br>' + str(response.json()["main"]["temp_max"])   

def what_is_traffic (location):
	endpoint = endpoint = "http://dev.virtualearth.net/REST/v1/Traffic/Incidents/mapArea/includeLocationCodes?severity=severity1,severity2,severityn&type=type1,type2,typen&key=BingMapsKey"+ location
	payload  = {"country_to_capital":"location"}
	response = requests.get(endpoint,params=payload)
	return response.json() 

@app.route("/")
def hello():
	return render_template("main.html")

@app.route("/countrydetail/<location>")
def countrydetail(location):
	capital = code_to_capital(location)
	weather = what_is_weather(capital)
	traffic = what_is_traffic(location)
	return render_template("countrydetail.html", capital = capital, weather = weather, traffic = traffic)

@app.route("/weather/<location>")
def weather(location):
	capital = code_to_capital(location)
	return str(what_is_weather(capital))



app.run(debug=True)

