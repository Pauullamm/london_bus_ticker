from flask import Flask, render_template
import requests

api_url = ""

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bus')
def api_get():
    r=requests.get('https://api.tfl.gov.uk/Mode/bus/Arrivals')
    return render_template('search.html', buses=r.json()[0])

if __name__ == '__main__':
    app.run(debug=True)
