import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def clean_data(train):
    #  Getting a feel for the data
    print(train.head())
    print(train.info())

    # Identify missing data
    # A large number of people have not entered their age
    # Cabin is not identifed for a vast majority
    # Embarked is missing for some
    #sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    #plt.show()

    # Data cleaning
    # We want to fill in missing age data.  We could use the overal average age but
    # a better estimate would may be to use traveling class as an indicator of age.
    # Notice on the following box plots how class 1 travelers were older on average
    #plt.figure(figsize=(12, 7))
    #sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')
    #plt.show()

    # We can deteermine the average age per class as follows:
    # print('Average age for class 1 passengers: {}'.format(train[train['Pclass']==1]['Age'].mean()))
    # print('Average age for class 2 passengers: {}'.format(train[train['Pclass']==2]['Age'].mean()))
    # print('Average age for class 3 passengers: {}'.format(train[train['Pclass']==3]['Age'].mean()))

    # Average age for class 1 passengers: 38.233440860215055
    # Average age for class 2 passengers: 29.87763005780347
    # Average age for class 3 passengers: 25.14061971830986

    # define a function to replace missing ages with average for travel class
    def impute_age(cols):
        age = cols[0]
        travel_class = cols[1]

        if pd.isnull(age):
            if travel_class == 1:
                return 38
            elif travel_class == 2:
                return 30
            else:
                return 25
        else:
            return age

    # Apply the function to the dataframe by columns (axis =1)
    train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)

    # confirm no more missing age data
    # sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    # plt.show()

    # Extracting surname information from name. First a function
    def extract_surname(cols):

        name = cols[0]

        if "mrs" in name.lower():
            return "mrs"
        elif "mr" in name.lower():
            return "mr"
        elif "miss" in name.lower():
            return "miss"
        elif "dr" in name.lower():
            return "dr"
        elif "master" in name.lower():
            return "master"
        elif "rev" in name.lower():
            return "rev"
        else:
            return "na"

    train['Surname'] = train[['Name']].apply(extract_surname, axis=1)

    # confirm no more missing age data
    sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.show()

    sns.set_style('whitegrid')
    sns.countplot(x='Surname', data=train, palette='RdBu_r')
    plt.show()

    surname = pd.get_dummies(train['Surname'],drop_first=True)
    train = pd.concat([train,surname],axis=1)

    # Mostly empty cabin column.  Drop cabin
    train.drop('Cabin',axis=1,inplace=True)

    # Select cases do not have embarked so we drop those rows
    train.dropna(inplace=True)

    # Creating dummie variables for sex and embarked
    sex = pd.get_dummies(train['Sex'],drop_first=True)
    embark = pd.get_dummies(train['Embarked'],drop_first=True)
    train = pd.concat([train,sex,embark],axis=1)

    # Remove columns not needed or analysis
    train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)

    print("Cleaned data information")
    print(train.head())
    print(train.info())

    # confirm cleaned data
    sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.show()

    return train

