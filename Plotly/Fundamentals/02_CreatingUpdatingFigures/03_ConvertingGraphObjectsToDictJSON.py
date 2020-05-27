# -*- coding: utf-8 -*-

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(height=600, width=800)
)

fig.layout.template = None # to slim down the output

print("\n\nDictionary Representation of A Graph Object:\n\n" + str(fig.to_dict()))
print("\n\n")
print("JSON Representation of A Graph Object:\n\n" + str(fig.to_json()))
print("\n\n")