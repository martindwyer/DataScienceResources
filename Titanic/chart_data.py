import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def chart_data(train):

    # confirm cleaned data
    sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.show()

    # Get ideas about correlations
    sns.heatmap(train.corr(), yticklabels=True, annot=True,  cbar=False, cmap='viridis')
    plt.show()

    # Getting an idea how many survived
    sns.set_style('whitegrid')
    sns.countplot(x='Survived',data=train,palette='RdBu_r')
    plt.show()

    # Further insight of survival and travel class
    sns.set_style('whitegrid')
    sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
    plt.show()



    # of siblings aboard
    sns.countplot(x='SibSp',data=train)
    plt.show()


    # of siblings aboard
    sns.countplot(x='Survived',hue='Q',data=train)
    plt.show()







