'''

ESYST-131 - Doves and Hawks

A. Suresh Kumar (5/1/22)

==================================

This program will define two dictionaries

each meant to represent a distinct type of bird

to be used in modeling the evolution and distribution

of aggressive behaviors.
==================================

Variables:

dove     # dictionary meant to model attributes and behaviors of an peaceful bird

hawk     # dictionary meant to model attributes and behaviors of an aggressive bird

==================================

Functions:

consumeFood    # find and consume a piece of food

reproduce      # create another bird of the same type

encounterBird  # defines behavior to occur when another bird is at the same food

==================================

Imports:

{None}

'''
#defines peaceful bird type
dove = {
    #number of generations the bird has survived since it was created
    "generationsLived": 0,
    #defines eating behavior for the bird type
    "eat": consumeFood(),
    #defines what to do when encountering another bird at the same food
    "encounterBird": doveEncounter(),
    #defines reproduction behavior to create another bird of the same type
    "reproduce": doveReproduce(),
    #stores whether bird has enough food to survive
    "minimumSurvivalFood": True,
    #stores whether bird has enough food to reproduce
    "minimumReproductionFood": False,
    #number to identify the bird
    "birdID": 0
}

#defines aggressive bird type
hawk = {
    #number of generations the bird has survived since it was created
    "generationsLived": 0,
    #defines eating behavior for the bird type
    "eat": consumeFood(),
    #defines what to do when encountering another bird at the same food
    "encounterBird": hawkEncounter(),
    #defines reproduction behavior to create another bird of the same type
    "reproduce": hawkReproduce(),
    #stores whether bird has enough food to survive
    "minimumSurvivalFood": True,
    #stores whether bird has enough food to reproduce
    "minimumReproductionFood": False,
    #number to identify the bird
    "birdID": 1
}