from pygraph.algorithms.searching import depth_first_search
# Import the module and instantiate a graph object
from pygraph.classes.graph import graph

gr = graph()
# Add nodes
gr.add_nodes(["X", "Y", "Z"])
gr.add_nodes(["A", "B", "C"])
# Add edges
gr.add_edge(("X", "Y"))
gr.add_edge(("X", "Z"))
gr.add_edge(("A", "B"))
gr.add_edge(("A", "C"))
gr.add_edge(("Y", "B"))
# Depth first search rooted on node X
st, pre, post = depth_first_search(gr, root="X")
# Print the spanning tree
print(st)


def nodes(graph, node):
    for y in graph[node]:
        yield y


for x in nodes(gr, "X"):
    print(x)
