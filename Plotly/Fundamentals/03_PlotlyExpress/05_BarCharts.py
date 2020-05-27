# -*- coding: utf-8 -*-
import plotly.express as px
df = px.data.tips()

df.info()
print(df.columns)

df['tip_percent'] = df['tip']/df['total_bill']

variables = ['total_bill', 'tip', 'tip_percent', 'sex', 'smoker', 'day', 'time', 'size']

for var in variables: 
    fig = px.histogram(df, x=var)
    fig.show()


fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df.columns)
fig.show()

fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
fig.show()

fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", facet_row="time", facet_col="day",
       category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
fig.show()