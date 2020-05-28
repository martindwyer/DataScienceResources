import pandas as pd

"""
1.  import the data 
"""
ecom = pd.read_csv('CourseExercises/datasets/ecommerce_purchases/purchases.csv')

"""
2. Check the head of the DataFrame
"""

print(ecom.head())

"""
3. How many rows are there? 
"""

print(ecom.info())

"""
4.  What is the average purchase price? 
"""

print("The average purchase price: ${:,.2f}".format(ecom['Purchase Price'].mean()))

"""
5. What are the highest and lowest purchase price? 
"""

print("The highest purchase price: {:,.2f}".format(ecom['Purchase Price'].max()))
print("The lowest purchase price: {:,.2f}".format(ecom['Purchase Price'].min()))

"""
6. How many people have 'en' as their language of choice on the website? 
"""
k = 0
for lang in ecom['Language']:
    if 'en' in lang:
        k += 1

print("{} people have English 'en' as their language".format(k))

"""
7.  How many have job title of 'Lawyer'? 
"""

print(ecom[ecom['Job'] == 'Lawyer'].count())

"""
8. How many people made the purchase during the AM and how many people made the purchase during PM ?
"""

print(ecom['AM or PM'].value_counts())

"""
9. What are the five most common job titles?
"""

print(ecom['Job'].value_counts().head(5))

"""
10. Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
"""

print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

"""
11. What is the email of the person with the following credit card:  4926535242672853
"""
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'].astype(str))

"""
12. How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?
"""

print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

"""
13. How many people have credit cards that expire in 2025?
"""

print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')))

"""
14. What are the five most popular email providers? 
"""

email_providers = ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

print(email_providers)
