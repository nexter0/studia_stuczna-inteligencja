from typing import Dict, List, Any, Callable
from edge import *


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = {}

    def __str__(self) -> str:
        string: str = ""
        for x in self.adjacencies:
            dest_val = [str(o.destination.data) for o in self.adjacencies[x]]
            string += f'| {str(x.data)} --> {dest_val} |'
        return string

    def create_vertex(self, data: Any) -> Vertex:
        new = Vertex(data)
        self.adjacencies[new] = []
        return new

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == EdgeType.undirected:
            self.adjacencies[source].append(Edge(source, destination, weight))
            self.adjacencies[destination].append(Edge(destination, source, weight))
        else:
            self.adjacencies[source].append(Edge(source, destination, weight))

    def traverse_breadth_first(self, first: Vertex, visit: Callable[[Any], None]) -> None:
        queue: List[Vertex] = []
        visited: List[Vertex] = []
        queue.append(first)
        visited.append(first)
        while len(queue) != 0:
            v = queue.pop()
            visit(v)
            for x in self.adjacencies[v]:
                if x.destination not in queue and x.destination not in visited:
                    visited.append(x.destination)
                    queue.append(x.destination)

    def shortest_path_to_vertex(self, start: Vertex, target: Vertex) -> Optional[List[Vertex]]:
        queue: List[List[Vertex]] = [[start]]
        visited: List[Vertex] = [start]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == target:
                return path
            for edge in self.adjacencies[node]:
                if edge.destination not in visited:
                    visited.append(edge.destination)
                    new_path = list(path)
                    new_path.append(edge.destination)
                    queue.append(new_path)
        return None

    def traverse_depth_first(self, first: Vertex, visit: Callable[[Any], None], visited: List[Vertex] = None) -> None:
        if visited is None:
            visited = []
        visit(first)
        visited.append(first)
        for x in self.adjacencies[first]:
            if x.destination not in visited:
                self.traverse_depth_first(x.destination, visit, visited)

    def show(self) -> None:
        print('digraph G {')
        for x in self.adjacencies:
            dest_val = [str(o.destination.data) for o in self.adjacencies[x]]
            for value in dest_val:
                print(f'{str(x.data)} -> {value}')
        print('}')