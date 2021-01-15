import json
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route("/")
def indexheaders():
  # get headers on request
  headers = {}
  for key,value in dict(request.headers).items():
    headers[key] = value
  # return response
  return jsonify(headers)
