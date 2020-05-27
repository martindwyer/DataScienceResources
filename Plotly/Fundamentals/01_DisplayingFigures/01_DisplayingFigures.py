# -*- coding: utf-8 -*-

import plotly.graph_objects as go
import pandas as pd


fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show(renderer='svg', width=800, height=600)
fig.show(renderer='iframe', width=800, height=600)


scores = [['Martin',10],
          ['Rose',10],
          ['Hollyann',7],
          ['Kyle',7],
          ['Casey',8],
          ['Noah',9]]

df = pd.DataFrame(data=scores,columns=['Name','Score'])

df.info()

fig = go.Figure(
    data=[go.Bar(y=df['Score'],x=df['Name'])],
    layout_title_text="Family score chart"
)
fig.show(renderer='svg', width=800, height=800)
fig.show(renderer='iframe', width=800, height=800)

