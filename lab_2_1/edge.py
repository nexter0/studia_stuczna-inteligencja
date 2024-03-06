from enum import Enum
from vertex import Vertex
from typing import Optional


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight