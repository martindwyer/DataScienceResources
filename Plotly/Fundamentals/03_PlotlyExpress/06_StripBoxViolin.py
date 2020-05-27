import plotly.express as px

df = px.data.tips()


fig = px.strip(df, x="total_bill", y="time", orientation="h", color="smoker")
fig.show()

fig = px.box(df, x="day", y="total_bill", color="smoker", notched=True)
fig.show()

fig = px.violin(df, y="tip", x="smoker", color="sex", box=True, points="all", hover_data=df.columns)
fig.show()

