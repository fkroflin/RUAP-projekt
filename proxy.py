from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

AZURE_ENDPOINT = "http://4a6cc3da-f855-4bdc-9bd9-96588ac98d95.northeurope.azurecontainer.io/score"
API_KEY = "spN3QTbUJnXuheBPTzveqlcZ7AucLTsb"

@app.route("/predict", methods=["POST"])
def predict():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post(AZURE_ENDPOINT, headers=headers, json=request.json)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(port=5000)
