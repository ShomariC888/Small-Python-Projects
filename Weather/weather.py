import requests as req
from pprint import pprint

API_Key = '3854a77d07e043ada384691967ec1587'
city = input("Enter a city: ")

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key +"&q="+ city

weather_data = req.get(base_url).json()

pprint(weather_data)
