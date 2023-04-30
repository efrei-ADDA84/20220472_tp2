import os
import requests

def get_weather(LAT,LONG, API_KEY):
	#api_key = api_key.strip('"')
	url= f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		weather = {
		'temperature': data['main']['temp'],
		'humidity': data['main']['humidity'],
		'description': data['weather'][0]['description']

		}
		return weather
	else:
		return 'Failed to get weather data. Error code: ' + str(response.status_code) + url

