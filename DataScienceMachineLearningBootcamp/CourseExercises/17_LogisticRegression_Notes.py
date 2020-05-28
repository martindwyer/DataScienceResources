# -*- coding: utf-8 -*-
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

train = pd.read_csv('CourseExercises/datasets/titanic/train.csv')

print(train.head())
train.info()

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived', hue="Sex", data=train)
plt.show()

sns.countplot(x='Survived', hue="Pclass", data=train)
plt.show()

sns.distplot(train['Age'].dropna(),kde=False,bins=30)
plt.show()

sns.countplot(x='SibSp', data=train)
plt.show()

sns.countplot(x='Parch', data=train)
plt.show()

train['Fare'].hist(bins=50)
plt.show()

sns.boxplot(x='Pclass',y='Age', data=train)

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1: 
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
    
train['Age'] =train[['Age','Pclass']].apply(impute_age,axis =1)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'])
train = pd.concat([train,sex,embark],axis=1)  

# dropping columns with too many NaN 
train.drop('Cabin',axis=1,inplace=True)
train.drop('Lifeboat',axis=1,inplace=True)
train.drop('Body',axis=1,inplace=True)

# dropping non-numeric data that are not helpful 
train.drop('PassengerId',axis=1,inplace=True)
train.drop('Name',axis=1,inplace=True)
train.drop('Sex',axis=1,inplace=True)
train.drop('Ticket',axis=1,inplace=True)
train.drop('Embarked',axis=1,inplace=True)
train.drop('WikiId',axis=1,inplace=True)
train.drop('Name_wiki',axis=1,inplace=True)
train.drop('Age_wiki',axis=1,inplace=True)
train.drop('Hometown',axis=1,inplace=True)
train.drop('Boarded',axis=1,inplace=True)
train.drop('Destination',axis=1,inplace=True)
train.drop('Class',axis=1,inplace=True)
train.dropna()
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
train.info()

print(train.head())

print(train.columns)

y = train['Survived']

X = train.drop('Survived',axis = 1)

logmodel = LogisticRegression()

logmodel.fit(X,y)

predictions = logmodel.predict(X)

print(classification_report(y,predictions))

print(confusion_matrix(y,predictions))



  


            
