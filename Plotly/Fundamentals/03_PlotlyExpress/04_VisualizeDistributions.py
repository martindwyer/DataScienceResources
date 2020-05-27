import plotly.express as px

df = px.data.iris()

fig = px.density_contour(df, x="sepal_width", y="sepal_length")
fig.show()


fig = px.density_contour(df, x="sepal_width", y="sepal_length", color="species", marginal_x="rug", marginal_y="histogram")
fig.show()

fig = px.density_heatmap(df, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram")
fig.show()