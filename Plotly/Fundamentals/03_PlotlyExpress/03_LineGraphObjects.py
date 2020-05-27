import plotly.express as px

df = px.data.gapminder()

df.info()

fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)
fig.show()


fig = px.line(df.query('country==["United States","China","Mexico","United Kingdom","Taiwan","Singapore","New Zealand"]'), 
              x="year", 
              y="lifeExp", 
              color="country", 
              line_group="country", 
              hover_name="country",
              line_shape="spline", 
              render_mode="svg")
fig.show()

fig = px.area(df.query('country=="United States"'), x="year", y="pop")
fig.show()


fig = px.area(df.query('country==["United States","Mexico","Canada"]'), 
              x="year", 
              y="pop",
              color="country")
fig.show()