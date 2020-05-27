import plotly.express as px

df = px.data.election()

df.info()

fig = px.scatter_ternary(df, 
                         a="Joly", 
                         b="Coderre", 
                         c="Bergeron", 
                         color="winner", 
                         size="total", 
                         hover_name="district",
                         size_max=15, 
                         color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"} )
fig.show()

fig = px.line_ternary(df, 
                         a="Joly", 
                         b="Coderre", 
                         c="Bergeron", 
                         color="winner",
                         line_dash="winner")
fig.show()