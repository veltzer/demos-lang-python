"""
A basic example of plotly

References:
- https://plot.ly/python/getting-started/ 
"""

from plotly.graph_objs import Data, Scatter
from plotly.offline import plot

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

plot(data, filename='/tmp/plotly.html', auto_open=False)
