# -*- coding: utf-8 -*-

import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="total_bill")
fig.show()


fig = px.histogram(df, x="day")
fig.show()

fig = px.histogram(df, x="total_bill", nbins=20)
fig.show()

