from flask import Flask, request
from TP01DEVOPS import get_weather
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    api_key = os.environ.get('API_KEY')
    weather_data = get_weather(lat, lon, api_key)
    return weather_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
