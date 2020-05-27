from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff

import datetime as dt

# monthly data

inflation = pd.read_csv('datasets/CPIAUCNS_PC1.csv')
inflation['DATE'] = inflation['DATE'].astype('datetime64[ns]')
inflation.set_index('DATE')


unemployment_rate = pd.read_csv('datasets/UNRATE.csv')
unemployment_rate['DATE'] = unemployment_rate['DATE'].astype('datetime64[ns]')
unemployment_rate.set_index('DATE')

three_month_treasury_bills = pd.read_csv('datasets/TB3MS.csv')
three_month_treasury_bills['DATE'] = three_month_treasury_bills['DATE'].astype('datetime64[ns]')
three_month_treasury_bills.set_index('DATE')

ten_year_treasury_rate = pd.read_csv('datasets/GS10.csv')
ten_year_treasury_rate['DATE'] = ten_year_treasury_rate['DATE'].astype('datetime64[ns]')
ten_year_treasury_rate.set_index('DATE')


industrial_production = pd.read_csv('datasets/INDPRO.csv')
industrial_production['PCT_CHG_INDPRO'] = industrial_production['INDPRO'].pct_change()*100
industrial_production['DATE'] = industrial_production['DATE'].astype('datetime64[ns]')
industrial_production.set_index('DATE')

"""
non_farm_payroll = pd.read_csv('datasets/PAYEMS.csv').set_index("DATE")
non_farm_payroll['DATE'] = non_farm_payroll['DATE'].astype('datetime64[ns]')
non_farm_payroll.set_index('DATE')



# quarterly data
gdp = pd.read_csv('datasets/GDP.csv').set_index("DATE",inplace= True)
real_gdp = pd.read_csv('datasets/GDPC1.csv').set_index("DATE",inplace= True)

"""



monthly_datasets = [unemployment_rate,three_month_treasury_bills,industrial_production]

monthly_data = inflation
for dataset in monthly_datasets:    
    monthly_data = pd.merge(monthly_data,dataset, on='DATE')

start = '2000-01-01'
end = '2020-04-01'

mask = (monthly_data['DATE'] > start) & (monthly_data['DATE'] <= end)

monthly_data = monthly_data.loc[mask]

monthly_data.info()


sns.heatmap(monthly_data.isnull(),yticklabels=False,cbar=False,cmap='viridis')

print(monthly_data)

columns = ['CPIAUCNS_PC1', 'UNRATE', 'TB3MS', 'PCT_CHG_INDPRO']
names = {'CPIAUCNS_PC1': 'Inflation Rate',
         'UNRATE': 'Unemployment Rate', 
         'TB3MS': '3 Mo. T-Bill Rate',
         'PCT_CHG_INDPRO': 'Industrial Production % Chg'}

fig = go.Figure([{
    'x': monthly_data['DATE'],
    'y': monthly_data[col],
    'name': names[col]
}  for col in columns])
fig.show()

for col in columns: 
    fig = px.histogram(monthly_data, x=col)
    fig.show()

fig = go.Figure(data=[
    go.Bar(name='Unemployment Rate', x=monthly_data['DATE'], y=monthly_data['UNRATE']),
    go.Bar(name='3 Month Treasury Rate', x=monthly_data['DATE'], y=monthly_data['TB3MS'])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()

correlations = monthly_data.corr().values

print(correlations)

for j in range(0, len(correlations[0])):
    for i in range(0,len(correlations[j])):
        correlations[j][i] = "%.2f" % correlations[j][i]

fig = ff.create_annotated_heatmap(correlations, colorscale='Viridis', showscale=True)
fig.show(renderer='iframe')

lm = LinearRegression()

X = monthly_data[['CPIAUCNS_PC1', 'TB3MS']]

y = monthly_data['UNRATE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)



