import json
from pureval.result import Result
from pureval.core import Validator


class json_str(Validator):
    """Parse a JSON string into a Python object."""
    def run(self, value, ctx):
        try:
            parsed = json.loads(value)
        except Exception:
            return Result(ok=False, errors=("invalid JSON",))
        return Result(ok=True, value=parsed)
