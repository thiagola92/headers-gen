from typing import Any
from packaging.version import Version


def find_best_option(version: str, options: tuple) -> Any | str | None:
    for v, o in options:
        if Version(version) >= Version(v):
            return o
    return None
