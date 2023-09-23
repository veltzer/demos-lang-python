"""
Doing a scatter with plotly express

References:
- https://plotly.com/python/line-and-scatter/
"""

import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
