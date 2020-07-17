from flask import Flask,request,make_response,jsonify
from flask_cors import CORS
from flask import redirect
from create_tree_json import get_tree_json_data
from create_json import get_map_json_data
import json

app=Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    return "Hello!"

@app.route("/api/tree",methods=["GET"])
def tree():
    cities=request.args.get("cities")
    year=request.args.get("y")
    month=request.args.get("m")
    day=request.args.get("d")
    json=jsonify(get_tree_json_data(cities,year,month,day))
    return json



@app.route("/api/map",methods=['GET'])
def map():
    cities=request.args.get("cities")
    year=request.args.get("y")
    month=request.args.get("m")
    day=request.args.get("d")
    json=jsonify(get_map_json_data(cities,year,month,day))
    return json