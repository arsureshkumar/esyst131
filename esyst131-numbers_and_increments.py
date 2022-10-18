
'''

ESYST-131 - Numbers and Increments

A. Suresh Kumar (4/3/22)

==================================

This program will print a list of numbers 

and brute-force increment each element by a number

of the user's choosing.

==================================

Variables:

inputList[]   # list containing inputted numbers

increment     # number that list will be incremented by

==================================

Functions:

{None}

==================================

Imports:

{None}

'''
#declares list variable to hold inputted numbers
inputList = []

#loop to take in inputted values
for i in range(5):

    #takes in and adds inputted values to the list
    inputList.append((int)(input('Enter your number: ')))

#displays list of inputted numbers
print('The numbers ' + (str)(inputList))

#takes in user-provided increment for inputted values
increment = (int)(input('How much would you like to increase? '))

#adds increment to each value of the inputlist
inputList = [x + increment for x in inputList]

#displays incremented values
print(inputList)

#displays sum of incremented values
print("The sum is: " + (str)(sum(inputList)))
