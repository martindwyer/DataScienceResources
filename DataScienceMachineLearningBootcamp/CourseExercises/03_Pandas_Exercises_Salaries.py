import numpy as np
import pandas as pd

"""
Data set for San Francisco city employee salaries, 2011 to 2014 taken from 
https://www.kaggle.com/kaggle/sf-salaries/data?select=Salaries.csv
"""

"""
1. import pandas as pd (see above)
"""

"""
2. Import data from csv file as dataframe.  Note that because there are a mix of numerics, blanks
and 'not provided' in the pay columns, conversion to numeric needed to be applied in a coerced 
context. 
"""

df = pd.read_csv('./sf-salaries/Salaries.csv', low_memory=False)

base_pay = df['BasePay']

df['BasePay'] = df['BasePay'].apply(pd.to_numeric, errors='coerce')
df['OvertimePay'] = df['OvertimePay'].apply(pd.to_numeric, errors='coerce')
df['OtherPay'] = df['OtherPay'].apply(pd.to_numeric, errors='coerce')
df['Benefits'] = df['Benefits'].apply(pd.to_numeric, errors='coerce')
df['TotalPay'] = df['TotalPay'].apply(pd.to_numeric, errors='coerce')
df['TotalPayBenefits'] = df['TotalPayBenefits'].apply(pd.to_numeric, errors='coerce')

"""
3. Check the head of the dataframe
"""

print(df.head())

"""
4.  Use the info() method to find out information about the data 
"""

print(df.info())

"""
5.  Find the mean of BasePay
"""

print("The mean base pay for a San Francisco employee is ${:,.2f}".format(df['BasePay'].mean()))

"""
6.  Find the maximum of OvertimePay
"""

print("The maximum overtime pay for a San Francisco employee is ${:,.2f}".format(df['OvertimePay'].max()))

"""
7. What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). 
"""

print("JOSEPH DRISCOLL's job title is {}".format(df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']))

"""
8. How much does Joseph Driscoll make?
"""

print("Joseph Driscoll makes {}".format(df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']))

"""
9. What is the name of the highest paid person?
"""

print("The highest paid person is {}".format(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]))

"""
10. What is the lowest amount of total pay with benefits?
"""

print(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].min()])

"""
11. What is the average pay for each year reported? 
"""

print(df.groupby('Year').mean()['TotalPay'])

"""
12. How many unique job titles are there? 
"""

print(df['JobTitle'].nunique())

"""
13. List the top five most frequently occuring job titles. 
"""

print(df['JobTitle'].value_counts().head(5))

"""
14. How many times does 'chief' appear in a job title? 
"""

job_titles = df['JobTitle']
k = 0
for title in job_titles:
    if 'chief' in title.lower():
        k += 1

print("{} job titles with 'chief'".format(k))

"""
15.  Is there a correlation between title length and compensation?
"""

df['title_len'] = df['JobTitle'].apply(len)

print(df[['title_len', 'TotalPayBenefits']].corr())
