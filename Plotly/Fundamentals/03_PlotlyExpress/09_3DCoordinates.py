# -*- coding: utf-8 -*-

import plotly.express as px
df = px.data.election()
fig = px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total", hover_name="district",
                  symbol="result", color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"})
fig.show()

fig = px.line_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner", line_dash="winner")
fig.show()


