import json
from functions.multiply.handler import handler


def test_handler():
    result = handler({"a": 3, "b": 3}, {})
    assert result == {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": 9}),
    }
