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
    return json.load(open("texts/texts.json"))

@app.route("/lstextfolder")
def lstextfolder():
    return "\n".join([i for i in os.listdir("texts") if os.path.isdir(f"texts/{i}")])


@app.route("/getdocument")
def getdocument():
    """TODO: add 440 in case file does not exist"""

    fname = request.args.get("doc")
    path = f"texts/{fname}/{fname}.html"
    return open(path, encoding="utf8").read()
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

@app.route("/getpos",methods=['POST'])
def getpos():
    out = []
    request_data = request.get_json()
    pos = request_data["pos"]
    fname =request_data["id_text"]
    text = json.load(open(f"texts/{fname}/{fname}.json"))
    for s_id, s_dict in text.items():
        for w_id, w_dict in s_dict.items():
            try:
                if w_dict["upos"] == pos:
                    out.append(w_id)
            except KeyError:
                pass
    return " ".join(out)
    #return text

if __name__ == "__main__":
    app.run(debug=True)

