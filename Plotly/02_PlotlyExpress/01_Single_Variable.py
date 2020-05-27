import plotly.express as px
import pandas as pd

df = px.data.tips()

df.info()

"""

Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   total_bill  244 non-null    float64
 1   tip         244 non-null    float64
 2   sex         244 non-null    object 
 3   smoker      244 non-null    object 
 4   day         244 non-null    object 
 5   time        244 non-null    object 
 6   size        244 non-null    int64  
dtypes: float64(2), int64(1), object(4)

"""

# plain scattergram of all the datapoints 
fig = px.scatter(df, y="tip")
fig.show()


df['tip_pct'] = df['tip']/df['total_bill']
fig = px.scatter(df, y="tip_pct")
fig.show()


# histogram for single variable

fig = px.histogram(df, x="total_bill")
fig.show()


fig = px.histogram(df, x="tip_pct")
fig.show()

