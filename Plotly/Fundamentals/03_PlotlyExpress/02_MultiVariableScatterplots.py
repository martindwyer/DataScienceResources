import plotly.express as px
import numpy as np

df = px.data.tips()

df['tip_percent'] = df['tip']/df['total_bill']

df.info()

fig = px.scatter_matrix(df)
fig.show()

fig = px.scatter_matrix(df, 
                        dimensions=["total_bill", "tip", "size", "tip_percent"],
                        color="smoker")
fig.show()

fig = px.scatter(df,
                 x='total_bill',
                 y="tip",
                 facet_col="sex",
                 facet_row="time",
                 color="smoker",
                 trendline="ols")
fig.show()


fig = px.scatter(df, 
                 x="total_bill", 
                 y="tip", 
                 facet_row="time", 
                 facet_col="day", 
                 color="smoker", 
                 trendline="ols",
                 category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
fig.show()


fig = px.scatter(df, 
                 x="total_bill", 
                 y="tip", 
                 color="size", 
                 facet_col="sex",
                 color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
fig.show(renderer='iframe')


fig = px.scatter(df, 
                 x="total_bill", 
                 y="tip", 
                 size="tip_percent", 
                 color="day",
                 hover_name="tip_percent", 
                 log_x=True, 
                 size_max=60)
fig.show(renderer='iframe')

fig = px.scatter(df, 
                 x="tip_percent", 
                 y="size", 
                 size="total_bill", 
                 color="day",
                 hover_name="tip_percent", 
                 log_x=True, 
                 size_max=60)
fig.show(renderer='iframe')