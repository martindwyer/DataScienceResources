import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

print(titanic.head())

# 1. Create a joint plot of age and fair paid

sns.jointplot(x='fare', y='age', data=titanic)
plt.show()

# 2. Create a distribution plot of far paid in 30 bins with no kde, color red

sns.distplot(titanic['fare'], bins=30, kde=False, color='red')
plt.show()

# 3. Create a box plot of traveling class and age with rainbow palette

sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
plt.show()

# 4. Create a count plot by sex

sns.countplot(x='sex', data=titanic)
plt.show()

# 5. Create a heat map for the correlations among all variables

sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.show()

# 6. Create two distribution plots side-by-side, one for male, one for female

g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')
plt.show()