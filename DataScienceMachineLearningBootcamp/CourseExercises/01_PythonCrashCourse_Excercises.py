"""
Created on Mon May 11 2020

@author: martin dwyer

Notes from python for data science
"""

"""
1. What is 7 to the power of 4
"""

print(7 ** 4)

"""
2. Split the string "Hi there Sam!" 
"""

print("Hi there Sam!".split(" "))

"""
3.  Given the variables:**

planet = "Earth"
diameter = 12742
** Use .format() to print the following string: **

The diameter of Earth is 12742 kilometers.
"""
planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers".format(planet, diameter))

"""
4. Given this nested list, use indexing to grab the word "hello" 
"""

lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

print(lst[3][1][2][0])

"""
5.  Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky 
"""

d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

"""
Detailed steps ...
inner_list = d.get('k1')
inner_dict = inner_list[3]
next_list = inner_dict.get('tricky')
final_dict = next_list[3]
hello = final_dict.get('target')[3]
"""

hello = d.get('k1')[3].get('tricky')[3].get('target')[3]

print(hello)

"""
6.  Main difference between a tuple and a list  
"""

# Tuple is immutable


"""
7. Create a function that grabs the email website domain from a string in the form: **

user@domain.com
"""

email = "user@domain.com"

print(email[email.index("@") + 1:])

"""
8. Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
"""


def find_dog(word: str):
    if "dog" in word.lower():
        return True
    else:
        return False


print(find_dog("The dog is running home!"))

print(find_dog("Dog is my friend's nick name"))

print(find_dog("I love my DOG!"))

print(find_dog("Ain't no d-g here!"))

"""
9. Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases
"""


def count_dogs(word: str) -> int:
    j = 0
    while "dog" in word.lower():
        j += 1
        word = word.replace("dog", "gone", 1)

    return j


print(count_dogs("How many times can you say dog? dog? dog?"))

print(count_dogs("How many times can you say dog? dog?"))

print(count_dogs("How many times can you say dog?"))

print(count_dogs("How many times can you say?"))

"""
10.  ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**

seq = ['soup','dog','salad','cat','great']
should be filtered down to:

['soup','salad'] 

"""

seq = ['soup', 'dog', 'salad', 'cat', 'great']

seq_revised = list(filter(lambda x: x[0].lower() == 's', seq))

print(seq_revised)


"""
11. Final Problem
*You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases. *

"""


def caught_speeding(speed: int, is_birthday: bool) -> str:
    ticket = ""
    if is_birthday:
        speed = speed - 5
    if speed <= 60:
        ticket = "No Ticket"
    elif speed <= 80:
        ticket = "Small Ticket"
    else:
        ticket = "Big Ticket"
    return ticket


print(caught_speeding(81,True))

print(caught_speeding(81,False))