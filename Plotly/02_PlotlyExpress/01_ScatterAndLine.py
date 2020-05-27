import plotly.express as px

df = px.data.iris()

# plain scattergram of all the datapoints 
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

# scattergram of all datapoints - colored based on their species
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()

# revised to lay histogram an rug on top of each axis
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
fig.show()

# revised to show trend line, box and whisker, and violin charts
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols")
fig.show()

df = px.data.tips()

# looking at plots of total bill and tip relations based on day of week and time of day
fig = px.scatter(df, x="total_bill", y="tip", facet_row="time", facet_col="day", color="smoker", trendline="ols",
          category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
fig.show()


df = px.data.iris()
# show relationship between all variables
fig = px.scatter_matrix(df)
fig.show()


# furtheer defining a scatter matrix
fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
fig.show()


# two scatter plots side by side for comparison
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="size", facet_col="sex",
           color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
fig.show()


# here the size of the data points change based on population and color based on continent
df = px.data.gapminder()
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
fig.show()
fig.show(renderer='iframe')


# STARTING LINE CHARTS WITH A CHART OF LIFE EXPECTANCY BY COUNTRY
fig = px.line(df, x="year", y="lifeExp", color="continent", line_group="country", hover_name="country",
        line_shape="spline", render_mode="svg")
fig.show()


# now mapping population as an area chart
fig = px.area(df, x="year", y="pop", color="continent", line_group="country")
fig.show()


