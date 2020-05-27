# -*- coding: utf-8 -*-

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=dict(title=dict(text="A Figure Specified By A Graph Object"))
)

fig.show()