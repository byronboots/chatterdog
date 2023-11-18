
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/call_palm_api', methods=['POST'])
def call_palm_api():
    # Get the input data from the request
    data = request.get_json()

    # Make a POST request to the PaLM API
    response = requests.post('https://api.palm.com/predict', json=data)

    # Return the response from the PaLM API
    return response.json()

if __name__ == '__main__':
    app.run()
