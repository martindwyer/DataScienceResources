# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:01:26 2020

@author: martin dwyer

Notes from python for data science
"""

"""
1. Import NumPy as Np
"""

import numpy as np

"""
2.  Create an array of 10 zeros
"""

arr = np.zeros(10)

print(arr)

"""
3. Create an array of ten ones.
"""

arr = np.ones(10)

print(arr)

""" 
4. Create an array of ten fives. 
"""

arr = np.ones(10)*5

print(arr)

"""
5. Create an array of the integers from 10 to 50
"""

arr = np.arange(10,51)

print(arr)

"""
6. Create an array of all the even integers from 10 to 50
"""

arr = np.arange(10,51,2)

print(arr)

""" 
7. Create a 3x3 matrix with values ranging from 0 to 8
"""

matrix = np.arange(0,9).reshape(3,3)

print(matrix)

"""
8. Create a 3x3 identity matrix
"""

matrix = np.eye(3)
print(matrix)

"""
9. Use NumPy to generate a random number between 0 and 1
"""

number = np.random.rand(1)

print(number)

"""
10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
"""

numbers = np.random.normal(0.0,1.0,25)

print(numbers)

"""
11. Create the following matrix
"""

matrix = np.arange(.01,1.01,.01).reshape(10,10)

print(matrix)

"""
12. Create an array of 20 linearly spaced points between 0 and 1:
"""

matrix = np.linspace(0, 1, 20)

print(matrix)

"""
13.  Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs
"""

# array
mat = np.arange(1,26).reshape(5,5)

print("full matrix")
print(mat)

print("\nThe last three lines, not including first column")
print(mat[2:,1:])

print("\nPulling out the number 20")
print(mat[3,4])

print("\nFirst three rows, second column")
print(mat[0:3, 1])

list_nums = []
for i in range(0,3):
    list_nums.append(mat[i,1])

print(np.array(list_nums))

print("\nThe last two rows")
print(mat[3:, :])

"""
14. Now do the following arithmetic with the matrix
"""

print("\nThe sum of all the values in mat")
print(np.sum(mat))

print("\nThe mean of all values in mat")
print(np.mean(mat))

print("\nThe standard deviation of all values in mat")
print(np.std(mat))

print("\nThe sum of all columns")
print(np.sum(mat, axis=0))

print("\nThe mean value for each column")
print(np.mean(mat, axis=0))

print("\nThe standard deviation for each column")
print(np.std(mat, axis=0))




