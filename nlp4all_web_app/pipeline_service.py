from flask import Flask, escape, request, jsonify
import sys
import os
import json
import utils
import pickle


app = Flask(__name__)

@app.route('/health')
def health():
    version = request.args.get("v", "2020-feb")
    if not version:
        return f'py-pypeline healthy!'
    return f'py-pipeline {escape(version)} healthy'

@app.route("/listtexts")
def listtexts():
    return "\n".join(os.listdir("texts"))
#    return {"mobydick":{"title": "Moby Dick" , 
#                        "author": "Melville"}}

@app.route("/getdocument")
def getdocument():
    """TODO: add 440 in case file does not exist"""

    fname = request.args.get("doc")
    path = f"texts/{fname}/{fname}.html"
    return open(path).read()
    #return open(f"texts/{doc}").read()

@app.route("/lstexts")
def lstexts():
    dirname = request.args.get("dirname")
    return "\n".join(os.listdir(f"texts/{dirname}"))

@app.route("/gettokeninfo")
def gettokeninfo():
    fname = request.args.get("doc")
    path = f"texts/{fname}/{fname}.json"
    tokenid = request.args.get("token")
    sentid = tokenid.split("_")[0]
    d = json.load(open(path))
    return d[sentid][tokenid]

if __name__ == "__main__":
    app.run(debug=True)
