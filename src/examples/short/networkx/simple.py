"""
Example of a graph using networkx

Notes:
- you can add nodes one by one
- you can add a whole container of nodes
- you don't have to add the nodes, adding edges will add the nodes if they are missing

References:
http://www.python-course.eu/networkx.php
"""

import networkx

G = networkx.Graph()
G.add_node('a')
G.add_nodes_from(['b', 'c'])

G.add_edge('d', 'e')
G.add_edge('a', 'b')

print('Nodes of graph:', G.nodes())
print('Edges of graph:', G.edges())
