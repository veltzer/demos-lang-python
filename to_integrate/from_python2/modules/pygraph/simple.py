"""
Example of a graph using pygraph

Notes:
- edges are added as tuples
- nodes must be added before edges to them can be attached
- pygraph.classes.graph is not directed
- pygraph.classes.digraph is directed

References:
https://code.google.com/p/python-graph/wiki/Example
"""

import pygraph.classes.graph

g = pygraph.classes.graph.graph()
g.add_node("a")
g.add_node("b")
g.add_nodes(["c", "d"])

g.add_edge(("a", "b"))
g.add_edge(("c", "b"))

print("number of nodes", len(g.nodes()))
print("number of edges", len(g.edges()))
print("nodes", g.nodes())
print("edges", g.edges())
