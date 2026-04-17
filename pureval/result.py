from dataclasses import dataclass, field


@dataclass(frozen=True)
class Result:
    ok: bool
    value: object = None
    errors: tuple = field(default_factory=tuple)
