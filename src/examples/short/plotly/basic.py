"""
A basic example of plotly

References:
- https://plot.ly/python/getting-started/
"""

import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('/tmp/plotly.html', auto_open=True)
