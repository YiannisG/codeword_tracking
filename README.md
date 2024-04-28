# Codeword Tracking
A simple python REST API to track codewords

## Installation
Create a new python 3.11 virtualenv

`pip install poetry==1.8.2`

`poetry install`

## Testing

`python -m pytest`

## Running locally

By default this runs on localhost, port 3000. By populating the FLASK_RUN_PORT environment variable on execution a different port can be selected.

`python app.py`

endpoints:

`/get-actions` - lists all codeword/action_id combinations

`/get-action-id`  (body) `{"codeword": <query integer>}` - retrieves single action id corresponding to specific codeword

`/get-codewords`  (body) `{"action_id": <query string>}` - retrieves all codewords 
