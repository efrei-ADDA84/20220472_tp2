from flask import Flask, request
from TP01DEVOPS import get_weather

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    api_key = request.args.get('api_key')
    weather_data = get_weather(lat, lon, api_key)
    return weather_data
if __name__ == '__main__':
    app.run(debug=True)

