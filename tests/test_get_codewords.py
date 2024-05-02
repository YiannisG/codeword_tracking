import json

from app import app


def test_existing_action_id():
    with app.test_client() as c:
        res = c.post("/get-codewords", json={"action_id": "thanks"})
        assert res.status_code == 200
        expected = {"result": [5002]}
        assert expected == json.loads(res.get_data(as_text=True))


def test_missing_action_id():
    with app.test_client() as c:
        res = c.post("/get-codewords", json={"action_id": "thanks2"})
        assert res.status_code == 200
        expected = {"result": []}
        assert expected == json.loads(res.get_data(as_text=True))


def test_incorrect_type_action_id():
    with app.test_client() as c:
        res = c.post("/get-codewords", json={"action_id": 105})
        assert res.status_code == 400
        expected = {"message": "improperly formatted body: 105 is not of type 'string'"}
        assert expected == json.loads(res.get_data(as_text=True))


def test_incorrectly_formatted_body():
    with app.test_client() as c:
        res = c.post("/get-codewords", json={"actidon_id": "thanks"})
        assert res.status_code == 400
        expected = {"message": "improperly formatted body: 'action_id' is a required property"}
        assert expected == json.loads(res.get_data(as_text=True))
