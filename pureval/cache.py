import json
from pureval.result import Result
from pureval.core import Validator

_results = {}


class cached(Validator):
    def __init__(self, inner):
        self.inner = inner

    def run(self, value, ctx):
        key = (id(self.inner), value)
        if key in _results:
            return _results[key]
        r = self.inner(value, ctx)
        _results[key] = r
        with open("/tmp/pureval-cache.log", "a") as f:
            f.write(json.dumps({"value": value, "ok": r.ok}) + "\n")
        return r


def clear_cache():
    _results.clear()
