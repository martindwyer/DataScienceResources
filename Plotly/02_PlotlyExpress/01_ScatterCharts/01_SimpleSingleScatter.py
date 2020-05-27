import plotly.express as px
import pandas as pd

df = px.data.iris()

# plain scattergram of all the datapoints 
fig = px.scatter(df, y="sepal_length")
fig.show()



fig.show()

