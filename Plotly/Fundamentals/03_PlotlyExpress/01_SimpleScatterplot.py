import plotly.express as px
df = px.data.iris()

df.info()

fig = px.scatter(df, 
                 x="sepal_width", 
                 y="sepal_length",
                 trendline="ols")
fig.show()

fig = px.scatter(df, 
                 x="sepal_width", 
                 y="sepal_length", 
                 trendline="ols",
                 color="species")

fig.show()


fig = px.scatter(df, 
                 x="sepal_width", 
                 y="sepal_length", 
                 color="species", 
                 trendline='ols',
                 marginal_x="histogram")
fig.show()


fig = px.scatter(df, 
                 x="sepal_width", 
                 y="sepal_length", 
                 color="species", 
                 trendline='ols',
                 marginal_x="histogram",
                 marginal_y='rug')
fig.show()


fig = px.scatter(df, 
                 x="sepal_width", 
                 y="sepal_length", 
                 color="species", 
                 trendline='ols',
                 marginal_x="box",
                 marginal_y='violin')
fig.show()
