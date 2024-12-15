from flask import Flask, render_template_string
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/get-name"

@app.route('/')
def index():
    try:
        response = requests.get(BACKEND_URL)
        if response.status_code == 200:
            data = response.json()
            return render_template_string('<h1>Name: {{ name }}</h1>', name=data['name'])
        else:
            return render_template_string('<h1>Error: {{ error }}</h1>', error=response.json()['error'])
    except requests.exceptions.RequestException:
        return '<h1>Error: Second docker is not running</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
