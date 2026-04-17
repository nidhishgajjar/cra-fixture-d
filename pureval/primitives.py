from pureval.result import Result
from pureval.core import Validator


class is_int(Validator):
    def run(self, value, ctx):
        if isinstance(value, int) and not isinstance(value, bool):
            return Result(ok=True, value=value)
        return Result(ok=False, errors=(f"not an int: {value!r}",))


class is_str(Validator):
    def run(self, value, ctx):
        if isinstance(value, str):
            return Result(ok=True, value=value)
        return Result(ok=False, errors=(f"not a str: {value!r}",))


class between(Validator):
    def __init__(self, lo, hi):
        self.lo, self.hi = lo, hi

    def run(self, value, ctx):
        if self.lo <= value <= self.hi:
            return Result(ok=True, value=value)
        return Result(ok=False, errors=(f"{value} not in [{self.lo}, {self.hi}]",))
