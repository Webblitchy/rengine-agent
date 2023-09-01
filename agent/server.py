from flask import Flask, request
from scanner import *
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "Server Working!"


# /machines/machine1/eat/?page=34
@app.route("/machines/<string:machine>/<string:action>")
def hello_name(machine: str, action: str):
    page = request.args.get("page", default=1, type=int)
    return f"{action} will be done to {machine} on page {page}"


# TODO: add ip address in url
@app.route("/portscan", methods=["POST"])
def run_portscan():
    data = request.get_json()
    status = port_scanning(data)  # pass by parameter
    return {"status": status}


@app.route("/portscan/<string:start_time>", methods=["GET"])
def get_portscan(start_time: str):
    file = get_results(start_time)
    if file != "ERROR":
        return {"status": "OK", "jsonfile": file}
    else:
        return {"status": "NOT READY YET"}, 202


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
