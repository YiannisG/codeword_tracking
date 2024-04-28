import json

from app import app


def test_get_all_actions():
    with app.test_client() as c:
        res = c.get("/get-actions")
        assert res.status_code == 200
        expected = [{"codeword": 5001, "id": "alert"}, {"codeword": 5002, "id": "thanks"}]
        assert expected == json.loads(res.get_data(as_text=True))
