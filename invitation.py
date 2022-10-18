
'''

ESYST-131 - Working with Lists

A. Suresh Kumar (5/2/22)

==================================

This program will print a series of iteratively

better invitations to a party based on a list

of friends

==================================

Variables:

friends[]   # a list to store all the names of invited friends

==================================

Functions:

{None}

==================================

Imports:

{None}
'''
# Task 1: creating a list variable with the given friend names, called "friends"
friends = [
    "johnny bravo", 
    "marilyn Monroe", 
    "Nikola Tesla", 
    "cleopatra", 
    "Steve rogers", 
    "helen of Troy", 
    "bruce bAnner", 
    "Natasha Romanoff"
]

# Task 2: printing the previously created friends list
print(friends)

# Task 3:

# Phase 1: print each element of the friends list individually on its own line
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
print(friends[6])
print(friends[7])

# Phase 2: print each element of the friends list individually on its own line split into a list of the names
print(friends[0].split(" "))
print(friends[1].split(" "))
print(friends[2].split(" "))
print(friends[3].split(" "))
print(friends[4].split(" "))
print(friends[5].split(" "))
print(friends[6].split(" "))
print(friends[7].split(" "))

# Phase 3: print each element's first name only from the friends list individually on its own line
print(friends[0].split(" ")[0])
print(friends[1].split(" ")[0])
print(friends[2].split(" ")[0])
print(friends[3].split(" ")[0])
print(friends[4].split(" ")[0])
print(friends[5].split(" ")[0])
print(friends[6].split(" ")[0])
print(friends[7].split(" ")[0])

# Task 4: capitalize each of the printed first names

print(friends[0].split(" ")[0].title())
print(friends[1].split(" ")[0].title())
print(friends[2].split(" ")[0].title())
print(friends[3].split(" ")[0].title())
print(friends[4].split(" ")[0].title())
print(friends[5].split(" ")[0].title())
print(friends[6].split(" ")[0].title())
print(friends[7].split(" ")[0].title())

# Task 5: use fstrings to add a jovial greeting

print(f"I sure hope you aren't late to my party, {friends[0].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[1].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[2].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[3].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[4].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[5].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[6].split(' ')[0].title()}!")
print(f"I sure hope you aren't late to my party, {friends[7].split(' ')[0].title()}!")