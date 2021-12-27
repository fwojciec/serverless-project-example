import json
from typing import Any, Dict

from serverless_project.count import Math


def handler(event: Dict[str, Any], _: object) -> Dict[str, Any]:
    math = Math()
    result = math.add(event["a"], event["b"])
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": result}),
    }
