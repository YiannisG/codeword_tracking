import os
import json

from flask import Flask, jsonify, request

actions_location = "actions.json"
app = Flask(__name__)

with open(actions_location) as fh:
    actions = json.load(fh)['actions']

FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 3000)
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", False)


@app.get("/show-actions")
def show_actions():
    return jsonify(actions)


@app.get("/get-action-id")
def get_action_id():
    codeword = int(request.get_json()['codeword'])
    for i in actions:
        if i['codeword'] == codeword:
            return jsonify(i['id'])


@app.get("/get-codewords")
def get_codeword():
    data = request.get_json()['action_id']
    return jsonify([entry['codeword'] for entry in actions if entry['id'] == data])


if __name__ == '__main__':
    print(FLASK_RUN_PORT)
    print(FLASK_DEBUG)
    app.run(port=FLASK_RUN_PORT, debug=FLASK_DEBUG)
