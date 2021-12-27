import json
from typing import Any, Dict

from serverless_project.count import Math


def handler(event: Dict[str, Any], _: object) -> Dict[str, Any]:
    math = Math()
    result = math.multiply(event["a"], event["b"])
    return {
        "statusCode": 200,
        "body": json.dumps({"answer": result}),
        "headers": {"Content-Type": "application/json"},
    }
