import json
from typing import Any, Dict

from shared.math import Multiplication


def handler(event: Dict[str, Any], _: object) -> Dict[str, Any]:
    multiplication = Multiplication()
    result = multiplication.multiply(event["a"], event["b"])
    return {
        "statusCode": 200,
        "body": json.dumps({"answer": result}),
        "headers": {"Content-Type": "application/json"},
    }
