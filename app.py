import os
import json

from jsonschema import validate, ValidationError
from flask import Flask, jsonify, request

actions_location = "actions.json"
app = Flask(__name__)

with open(actions_location) as fh:
    actions = json.load(fh)["actions"]

FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 3000)
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", False)

GET_ACTION_ID_SCHEMA = {
    "type": "object",
    "properties": {
        "codeword": {"type": "integer"},
    },
    "required": ["codeword"]
}

GET_CODEWORDS_SCHEMA = {
    "type": "object",
    "properties": {
        "action_id": {"type": "string"},
    },
    "required": ["action_id"]
}


@app.get("/get-actions")
def get_actions():
    """ Retrieves all codewords and actions in the json file """
    return jsonify({"result": actions})


@app.get("/get-action-id")
def get_action_id():
    """ Looks up codeword in json input file and retrieves the action associated with it """
    data = request.get_json()
    try:
        validate(data, GET_ACTION_ID_SCHEMA)
    except ValidationError as e:
        return jsonify({"message": f"improperly formatted body: {e.message}"}), 400
    codeword = data["codeword"]
    for action in actions:
        if action["codeword"] == codeword:
            return jsonify({"result": action["id"]})
    return jsonify({"message": f"codeword: {codeword} does not exist"}), 400


@app.get("/get-codewords")
def get_codeword():
    """ Looks up action_id in json input file and retrieves all codewords that match it """
    data = request.get_json()
    try:
        validate(data, GET_CODEWORDS_SCHEMA)
    except ValidationError as e:
        return jsonify({"message": f"improperly formatted body: {e.message}"}), 400
    action_id = data["action_id"]
    search = [entry["codeword"] for entry in actions if entry["id"] == action_id]
    return jsonify({"result": search})


if __name__ == "__main__":
    app.run(port=FLASK_RUN_PORT, debug=FLASK_DEBUG)
