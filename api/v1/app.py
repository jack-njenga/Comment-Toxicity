#!/usr/bin/env python3
"""
api routes and their functionality
"""

from flask import Flask, abort, jsonify, request, make_response
from flask_cors import CORS
from xtoxica import Toxicity_model
import os


app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": "*"}})

XToxica = Toxicity_model()


@app.errorhandler(404)
def not_found(error):
    """
    returns a JSON-formatted 404 status code response
    """
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app.route("/api/v1", methods=["GET"], strict_slashes=False)
def api_ready():
    """
    api are you ready
    """
    return jsonify({"status": "OK"})

@app.route("/api/v1/help", methods=["GET"], strict_slashes=False)
def help():
    """
    help documentation
    """
    response = {"About XToxica api": "XToxica is an api that will help you filter toxic comments based on the level of toxicity you choose",
                "api routes": {
                    "GET /xtoxica/predict": "returns the predictions",
                    "GET /xtoxica/predict/<toxicity level>": "returns the prediction of a comment on <toxicity_level>"
                }}
    return jsonify(response)

@app.route("/api/v1/xtoxica/predict", methods=["GET", "POST"], strict_slashes=False)
def predict():
    """
    returns the prediction
    """
    data = request.get_json(silent=True)
    if data:
        # get the first only (one request at a time pls)
        keys = list(data.keys())
        comment = data[keys[0]]
        pred = XToxica.xtoxica(str(comment))

        print(f"------------ {comment} -------------")
        print(f"------------ {pred} -------------")

        return jsonify({"prediction": pred})
    else:
        abort(400, description="Not a JSON")

@app.route("/api/v1/xtoxica/<comment>", methods=["GET"], strict_slashes=False)
def predict_raw_comment(comment):
    """
    returns the prediction
    """
    if comment:
        comment = str(comment)
        pred = XToxica.xtoxica(comment)
        response = {"prediction": pred}

        print(f"------------ {comment} -------------")
        print(f"------------ {pred} -------------")

        return jsonify(response)
    else:
        abort(400, description="Not a JSON")

if __name__ == "__main__":
    port = 5005
    host = "0.0.0.0"

    app.run(host=host, port=port, threaded=True, debug=True)
