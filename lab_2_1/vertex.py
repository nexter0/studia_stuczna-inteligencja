from typing import Any


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any):
        self.data = data

    def __str__(self) -> str:
        return str(self.data)