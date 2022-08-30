from flask import Flask, render_template
import requests

api_url = ""

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bus', methods=['POST'])
def bus():
    r=requests.get('https://api.tfl.gov.uk/Mode/bus/Arrivals')
    bus_data = r.json()
    return render_template('index.html', buses=bus_data[0])

if __name__ == '__main__':
    app.run(debug=True)
