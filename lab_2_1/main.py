from graph import Graph

graph = Graph()
a0 = graph.create_vertex("A0")
a1 = graph.create_vertex("A1")
b0 = graph.create_vertex("B0")
b1 = graph.create_vertex("B1")
c0 = graph.create_vertex("C0")
c1 = graph.create_vertex("C1")
d0 = graph.create_vertex("D0")
d1 = graph.create_vertex("D1")
graph.add_undirected_edge(a0, a1)
graph.add_directed_edge(a0, c0)
graph.add_undirected_edge(c0, c1)
graph.add_directed_edge(c1, d1)
graph.add_directed_edge(a1, b1)
graph.add_undirected_edge(b1, b0)
graph.add_directed_edge(b0, d0)
graph.add_undirected_edge(d0, d1)

path = graph.shortest_path_to_vertex(a0, d0)
for vertex in path:
    print(vertex)


# print(graph)
# graph.show()