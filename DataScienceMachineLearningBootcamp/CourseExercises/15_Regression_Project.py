from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# get dataset
df = pd.read_csv('CourseExercises/ecommerce-data/ecommerce-data.csv')


# print descriptive information about the dataset
print(df.head())
df.info()
print(df.describe())


# print corrlations among all the variable, pairplot of the entire data set, and heatmap
df.corr()
sns.pairplot(df, kind="reg")
plt.show()
sns.heatmap(df.corr(), annot=True)
plt.show()


# print a histogram of the variable you are trying to predict
sns.distplot(df['Yearly Amount Spent'])
plt.show()


# do plots for variables where looking for impact
sns.jointplot(data=df,x='Time on Website', y = 'Yearly Amount Spent')
sns.jointplot(data=df,x='Time on App', y = 'Yearly Amount Spent')
sns.jointplot(data=df,x='Time on App', y = 'Length of Membership', kind='hex')
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent', data=df)


# print the column array and select columns for X and y
print(df.columns)
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

# use sklear to obtain test and training sets of data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# perform regression on training data 
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)

# put coefficients into array and print the array
cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
print(cdf)


"""
PART 2:  MAKING PREDICTIONS FROM THE TEST SET

"""

# get the model predictions using test data
predictions = lm.predict(X_test)

# print a scattergram of actual y test data and predications produced by the model
plt.scatter(y_test, predictions)
plt.xlabel('Y Test (True Values)')
plt.ylabel('Predicted Values')
plt.show()

# print a histogram of the errors - hoping to see a normal distribution
sns.distplot((y_test - predictions),bins=50)
plt.show()


# print error factors for interpretation:
print("\n\nMean absolute error: {}".format(metrics.mean_absolute_error(y_test, predictions)))
print("Mean squared error: {}".format(metrics.mean_squared_error(y_test, predictions)))
print("Root of mean squared error: {}".format(np.sqrt(metrics.mean_squared_error(y_test, predictions))))

print("r-squared: {}".format(metrics.explained_variance_score(y_test, predictions)))



"""
The following is a path to boston data for further exploration.

from sklearn.datasets import load_boston

boston = load_boston()
boston.keys()
print(boston['DESCR'])

"""
