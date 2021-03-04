from clean_data import clean_data
from chart_data import chart_data
from logistic_regression import logistic_regression
from deep_learning import deep_learning

import pandas as pd

#  Getting the training data
train = pd.read_csv('data/train.csv')

train = clean_data(train)

chart_data(train)

logistic_regression(train)

deep_learning(train)



