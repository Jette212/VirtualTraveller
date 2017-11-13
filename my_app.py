import json
import requests
from flask import Flask, render_template

app = Flask('MyApp')


def code_to_capital(code):
    endpoint = 'https://restcountries.eu/rest/v2/alpha/' + code
    response = requests.get(endpoint)
    return response.json()['capital']


def code_to_name(code):
    endpoint = 'https://restcountries.eu/rest/v2/alpha/' + code
    response = requests.get(endpoint)
    return response.json()['name']


def code_to_language(code):
    endpoint = 'https://restcountries.eu/rest/v2/alpha/' + code
    response = requests.get(endpoint)
    return response.json()['languages'][0]['name']


def what_is_weather(location):
    endpoint = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'q': location, 'units': 'metric',
               'appid': '3b503bfa7ea64695d425e95faf892625'}
    response = requests.get(endpoint, params=payload)

    return [response.json()['weather'][0]['description'].title(),
        str(response.json()['main']['temp']),
        str(response.json()['main']['temp_min']),
        str(response.json()['main']['temp_max'])]


def what_is_population(location):
    endpoint = 'https://restcountries.eu/rest/v2/alpha/' + location
    response = requests.get(endpoint)
    return response.json()['population']


def country_currency(location):
    endpoint = 'https://restcountries.eu/rest/v2/alpha/' + location
    response = requests.get(endpoint)
    return [response.json()['currencies'][0]['name'].title(),
    	response.json()['currencies'][0]['symbol']]


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/countrydetail/<location>')
def countrydetail(location):
    capital = code_to_capital(location)
    weather = what_is_weather(capital)
    population = '{:,}'.format(what_is_population(location))
    name = code_to_name(location)
    languages = code_to_language(location)
    currency = country_currency(location)
    return render_template(
        'countrydetail.html',
        capital=capital,
        weather=weather,
        languages=languages,
        name=name,
        population=population,
        currency=currency,
        )


@app.route('/weather/<location>')
def weather(location):
    capital = code_to_capital(location)
    return str(what_is_weather(capital))

app.run(debug=True)