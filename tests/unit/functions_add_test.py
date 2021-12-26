import json
from functions.add.handler import handler


def test_handler():
    result = handler({"a": 2, "b": 2}, {})
    assert result == {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": 4}),
    }
