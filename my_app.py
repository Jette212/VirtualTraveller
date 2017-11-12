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
	response = requests.get(endpoint, params=payload)
	return response.json()["weather"][0]["description"] + '\n' + str(response.json()["main"]["temp"]) + '\n' + str(response.json()["main"]["temp_min"]) + '\n' + str(response.json()["main"]["temp_max"])   
	

def what_is_traffic (location):
	endpoint = "http://dev.virtualearth.net/REST/v1/Traffic/Incidents/mapArea/includeLocationCodes?severity=severity1,severity2,severityn&type=type1,type2,typen&key=BingMapsKey"+ location
	payload  = {"country_to_capital":"location"}
	response = requests.get(endpoint,params=payload)
	return response.json() 

def country_news(location):
	endpoint = "https://newsapi.org/v1/sources?apiKey=80fb8990d33c49128aab4e2a2990583b&country=" + location
	response = requests.get(endpoint)
	return response.json() ["sources"][0]["description"] + '\n' + str(response.json()["sources"][0]["url"])


@app.route("/")
def hello():
	return render_template("main.html")

@app.route("/countrydetail/<location>")
def countrydetail(location):
	capital = code_to_capital(location)
	weather = what_is_weather(capital)
	traffic = what_is_traffic(location)	
	news = country_news(location) 
	return render_template("countrydetail.html", capital = capital, weather = weather, traffic = traffic, news = news) #news = pretty_news,)

@app.route("/weather/<location>")
def weather(location):
	capital = code_to_capital(location)
	return str(what_is_weather(capital))





#API for exchange rates
#20580abfe5aa991c3c0c67bf5b6c3f25

#API for news: 80fb8990d33c49128aab4e2a2990583b

app.run(debug=True)

