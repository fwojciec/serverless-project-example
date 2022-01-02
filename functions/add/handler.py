import json
from typing import Any, Dict

from shared.math import Addition


def handler(event: Dict[str, Any], _: object) -> Dict[str, Any]:
    addition = Addition()
    result = addition.add(event["a"], event["b"])
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": result}),
    }
