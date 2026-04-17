from pureval.result import Result


class Validator:
    def __call__(self, value, ctx=None):
        return self.run(value, ctx or {})

    def run(self, value, ctx):
        raise NotImplementedError


def compose(*validators):
    def runner(value, ctx=None):
        ctx = ctx or {}
        errors = []
        current = value
        for v in validators:
            r = v(current, ctx)
            if not r.ok:
                errors.extend(r.errors)
                return Result(ok=False, errors=tuple(errors))
            current = r.value
        return Result(ok=True, value=current)
    return runner
