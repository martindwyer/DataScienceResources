from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.graph_objs as go
import plotly.express as px


# # Logistic Regression Project - Solutions
# 
# In this project we will be working with a fake advertising data set, indicating whether or not a particular internet user clicked on an Advertisement on a company website. We will try to create a model that will predict whether or not they will click on an ad based off the features of that user.
# 
# This data set contains the following features:
# 
# * 'Daily Time Spent on Site': consumer time on site in minutes
# * 'Age': cutomer age in years
# * 'Area Income': Avg. Income of geographical area of consumer
# * 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
# * 'Ad Topic Line': Headline of the advertisement
# * 'City': City of consumer
# * 'Male': Whether or not consumer was male
# * 'Country': Country of consumer
# * 'Timestamp': Time at which consumer clicked on Ad or closed window
# * 'Clicked on Ad': 0 or 1 indicated clicking on Ad
# 
# **Import a few libraries you think you'll need (Or just import them as you go along!)**



# ## Get the Data
# **Read in the advertising.csv file and set it to a data frame called ad_data.**

ad_data = pd.read_csv('CourseExercises/datasets/advertising-data/advertising.csv')


ad_data['Clicked'] = ad_data['Clicked on Ad'].apply(lambda x: 'True' if x == 1 else 'False')

columns = ['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country','Timestamp', 'Clicked on Ad', 'Clicked']

numeric_columns = columns = ['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage']

# printing descriptive stats for web display
for col in numeric_columns: 
    print('<tr>')
    print('<td>' + f"{col}" + '</td>')
    print(f'<td>{ad_data[col].mean():,.3f}</td>')
    print(f'<td>{ad_data[col].std():,.3f}</td>')
    print(f'<td>{ad_data[col].min():,.3f}</td>')
    print(f'<td>{ad_data[col].max():,.3f}</td>')
    print('</tr>')


# **Check the head of ad_data**
print(ad_data.head())


# ** Use info and describe() on ad_data**
ad_data.info()

print(ad_data.describe())

# ## Exploratory Data Analysis
# 
# Let's use seaborn to explore the data!
# 
# Try recreating the plots shown below!
# 
# ** Create a histogram of the Age**


fig = px.histogram(ad_data, x="Daily Time Spent on Site", labels={'x': 'Daily Time Spent on Site', 'y': 'count'})
fig.update_layout(
    title_text='Daily Time on Site', # title of plot
    xaxis_title_text='Time', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.0, # gap between bars of adjacent location coordinates
    bargroupgap=0.05 # gap between bars of the same location coordinates
)
fig.show()


fig = px.histogram(ad_data, x="Daily Internet Usage", nbins=30, labels={'x': 'Daily Internet Usage', 'y': 'count'})
fig.update_layout(
    title_text='Daily Inernet Usage', # title of plot
    xaxis_title_text='Time', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.0, # gap between bars of adjacent location coordinates
    bargroupgap=0.05 # gap between bars of the same location coordinates
)
fig.show()


fig = px.histogram(ad_data, x="Area Income", nbins=30, labels={'x': 'Area Income', 'y': 'count'})
fig.update_layout(
    title_text='Income for Sample Group', # title of plot
    xaxis_title_text='Income', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.0, # gap between bars of adjacent location coordinates
    bargroupgap=0.05 # gap between bars of the same location coordinates
)
fig.show()


fig = px.histogram(ad_data, x="Age", nbins=30, labels={'x': 'Age', 'y': 'count'})
fig.update_layout(
    title_text='Customer Age in Years', # title of plot
    xaxis_title_text='Age of Customer', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.0, # gap between bars of adjacent location coordinates
    bargroupgap=0.05 # gap between bars of the same location coordinates
)
fig.show(renderer='iframe')

drop_columns = columns = ['Ad Topic Line', 'City', 'Male', 'Country','Timestamp','Clicked']

num_data = ad_data.copy(deep=True)

for col in drop_columns:
    num_data.drop(col, axis=1, inplace=True)

sns.heatmap(num_data.corr(), annot=True)
plt.show()


# **Create a jointplot showing Area Income versus Age.**
fig = px.scatter(ad_data, x="Age", y="Area Income", color="Clicked", marginal_y="histogram", marginal_x="histogram", trendline="ols")
fig.update_layout(
    title_text='Relation Between Customer Age and Area Income', # title of plot
    xaxis_title_text='Age of Customer', # xaxis label
    yaxis_title_text='Area Income', # yaxis label
)
fig.show()

# **Create a jointplot showing the kde distributions of Daily Time spent on site vs. 
fig = px.density_contour(ad_data, x="Age", y="Daily Time Spent on Site",marginal_y="histogram", marginal_x="histogram")
fig.update_layout(
    title_text='Relation Between Customer Age and Time Spent on Site', # title of plot
    xaxis_title_text='Age of Customer', # xaxis label
    yaxis_title_text='Time Spent on Site Daily', # yaxis label
)

fig.show()


# ** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**
fig = px.scatter(ad_data, x="Daily Time Spent on Site", y="Daily Internet Usage", marginal_y="histogram", marginal_x="histogram", color='Clicked', trendline="ols")
fig.update_layout(
    title_text='Relation Between Time Spent on Site and Internet Usage', # title of plot
    xaxis_title_text='Daily Time on Site', # xaxis label
    yaxis_title_text='Daily Internet Usage', # yaxis label
)

fig.show()


# ** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**

fig = px.scatter_matrix(ad_data, dimensions=["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage"],color="Clicked")
fig.show()

# # Logistic Regression
# 
# Now it's time to do a train test split, and train our model!
# 
# You'll have the freedom here to choose columns that you want to train on!

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# ** Train and fit a logistic regression model on the training set.**

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)


# ## Predictions and Evaluations
# ** Now predict values for the testing data.**

predictions = logmodel.predict(X_test)


# ** Create a classification report for the model.**
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

print(logmodel.coef_,logmodel.intercept_)


