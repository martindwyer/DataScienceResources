from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# get dataset
df = pd.read_csv('CourseExercises/datasets/housing-data/USA_Housing.csv')


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
sns.distplot(df['Price'])
plt.show()

# print the column array and select columns for X and y
# print(df.columns)
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
        'Area Population']]
y = df['Price']

# use sklear to obtain test and training sets of data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

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
plt.show()

# print a histogram of the errors - hoping to see a normal distribution
sns.distplot((y_test - predictions))
plt.show()


# print error factors for interpretation:
print("\n\nMean absolute error: {}".format(metrics.mean_absolute_error(y_test, predictions)))
print("Mean squared error: {}".format(metrics.mean_squared_error(y_test, predictions)))
print("Root of mean squared error: {}".format(np.sqrt(metrics.mean_squared_error(y_test, predictions))))


"""
The following is a path to boston data for further exploration.

from sklearn.datasets import load_boston

boston = load_boston()
boston.keys()
print(boston['DESCR'])

"""