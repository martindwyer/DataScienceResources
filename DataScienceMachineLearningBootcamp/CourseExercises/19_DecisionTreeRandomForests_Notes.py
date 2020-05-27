#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Decision Trees and Random Forests in Python

# This is the code for the lecture video which goes over tree methods in Python. Reference the video lecture for the full explanation of the code!
# 
# I also wrote a [blog post](https://medium.com/@josemarcialportilla/enchanted-random-forest-b08d418cb411#.hh7n1co54) explaining the general logic of decision trees and random forests which you can check out. 
# 
# ## Import Libraries

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data

# In[5]:


df = pd.read_csv('CourseExercises/kyphosis-data/kyphosis.csv')


# In[7]:


df.head()
df.info()


# ## EDA
# 
# We'll just check out a simple pairplot for this small dataset.

# In[10]:


sns.pairplot(df,hue='Kyphosis',palette='Set1')


# ## Train Test Split
# 
# Let's split up the data into a training set and a test set!

# In[11]:


from sklearn.model_selection import train_test_split


# In[12]:


X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']


# In[21]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)


# ## Decision Trees
# 
# We'll start just by training a single decision tree.

# In[14]:


from sklearn.tree import DecisionTreeClassifier


# In[15]:


dtree = DecisionTreeClassifier()


# In[22]:


dtree.fit(X_train,y_train)


# ## Prediction and Evaluation 
# 
# Let's evaluate our decision tree.

# In[23]:


predictions = dtree.predict(X_test)


# In[24]:


from sklearn.metrics import classification_report,confusion_matrix


# In[25]:


print(classification_report(y_test,predictions))


# In[20]:


print(confusion_matrix(y_test,predictions))


# ## Tree Visualization
# 
# Scikit learn actually has some built-in visualization capabilities for decision trees, you won't use this often and it requires you to install the pydot library, but here is an example of what it looks like and the code to execute this:

# See Jupyter notebook for illustrations which require substantive downloads

# ## Random Forests
# 
# Now let's compare the decision tree model to a random forest.

# In[26]:


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)


# In[27]:


rfc_pred = rfc.predict(X_test)


# In[28]:


print(confusion_matrix(y_test,rfc_pred))


# In[29]:


print(classification_report(y_test,rfc_pred))


# # Great Job!
