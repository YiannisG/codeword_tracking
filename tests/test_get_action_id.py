import json

from app import app


def test_existing_codeword():
    with app.test_client() as c:
        res = c.get("/get-action-id", json={"codeword": 5001})
        assert res.status_code == 200
        expected = {"result": "alert"}
        assert expected == json.loads(res.get_data(as_text=True))


def test_missing_codeword():
    with app.test_client() as c:
        res = c.get("/get-action-id", json={"codeword": 999})
        assert res.status_code == 400
        expected = {"message": "codeword: 999 does not exist"}
        assert expected == json.loads(res.get_data(as_text=True))


def test_incorrect_type_codeword():
    with app.test_client() as c:
        res = c.get("/get-action-id", json={"codeword": "999"})
        assert res.status_code == 400
        expected = {"message": "improperly formatted body: '999' is not of type 'integer'"}
        assert expected == json.loads(res.get_data(as_text=True))


def test_incorrectly_formatted_body():
    with app.test_client() as c:
        res = c.get("/get-action-id", json={"codesword": 5001})
        assert res.status_code == 400
        expected = {"message": "improperly formatted body: 'codeword' is a required property"}
        assert expected == json.loads(res.get_data(as_text=True))
