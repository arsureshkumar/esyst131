'''

ESYST-131 - Mad Lib

A. Suresh Kumar (4/3/22)

==================================

This program will create a madlib for the user

by taking in input strings and inserting them into a 

larger story string.

==================================

Variables:

adjectiveList[]   # list containing all available adjectives

sillyWord  # contains inputted silly word

lastName   # contains inputted last name

illness    # contains inputted illness

noun       # contains inputted noun (plural)

sillyWord2 # contains inputted second silly word

place      # contains inputted place

number     # contains inputted number

==================================

Functions:

randAdj       # returns a random adjective from the list adjectiveList

==================================

Imports:

random

'''
import random

sillyWord = input("Silly Word 1: ")
lastName = input("Last Name: ")
illness = input("illness:")
noun = input("Noun (plural): ")
sillyWord2 = input("Silly Word 2: ")
place = input("Place: ")
number = input("Number (Does not need to be converted to int): ")

adjectiveList = [
"adorable", " adventurous", " aggressive",
"agreeable", " alert", " alive",
"amused", " angry", " annoyed",
"annoying", " anxious", " arrogant",
"ashamed", " attractive", " average",
"awful", " bad", " beautiful",
"better", " bewildered", " black",
"bloody", " blue", " blue-eyed",
"blushing", " bored", " brainy",
"brave", " breakable", " bright",
"busy", " calm", " careful",
"cautious", " charming", " cheerful",
"clean", " clear", " clever",
"cloudy", " clumsy", " colorful",
"combative", " comfortable", " concerned",
"condemned", " confused", " cooperative",
"courageous", " crazy", " creepy",
"crowded", " cruel", " curious",
"cute", " dangerous", " dark",
"dead", " defeated", " defiant",
"delightful", " depressed", " determined",
"different", " difficult", " disgusted",
"distinct", " disturbed", " dizzy",
"doubtful", " drab", " dull",
"eager","easy","elated",
"elegant","embarrassed","enchanting",
"encouraging","energetic","enthusiastic",
"envious","evil","excited",
"expensive","exuberant","fair",
"faithful","famous","fancy",
"fantastic","fierce","filthy",
"fine","foolish","fragile",
"frail","frantic","friendly",
"frightened","funny","gentle",
"gifted","glamorous","gleaming",
"glorious","good","gorgeous",
"graceful","grieving","grotesque",
"grumpy","handsome","happy",
"healthy","helpful","helpless",
"hilarious","homeless","homely",
"horrible","hungry","hurt",
"ill","important","impossible",
"inexpensive","innocent","inquisitive",
"itchy","jealous","jittery",
"jolly","joyous","kind",
"lazy","light","lively",
"lonely","long","lovely",
"lucky","magnificent","misty",
"modern","motionless","muddy",
"mushy","mysterious","nasty",
"naughty","nervous","nice",
"nutty","obedient","obnoxious",
"odd","old-fashioned","open",
"outrageous","outstanding","panicky",
"perfect","plain","pleasant",
"poised","poor","powerful",
"precious","prickly","proud",
"putrid","puzzled","quaint",
"real","relieved","repulsive",
"rich","scary","selfish",
"shiny","shy","silly",
"sleepy","smiling","smoggy",
"sore","sparkling","splendid",
"spotless","stormy","strange",
"stupid","successful","super",
"talented","tame","tasty",
"tender","tense","terrible",
"thankful","thoughtful","thoughtless",
"tired","tough","troubled",
"ugliest","ugly","uninterested",
"unsightly","unusual","upset",
"uptight","vast","victorious",
"vivacious","wandering","weary",
"wicked","wide-eyed","wild",
"witty","worried","worrisome",
"wrong","zany","zealous"
]

def randAdj():
    return(adjectiveList[random.randint(0, len(adjectiveList) - 1)])

print(f'''Dear School Nurse:
{sillyWord} {lastName} will not be attending school today. 

He/she has come down with a case of {illness} and has horrible {noun} and a/an {randAdj()} fever. 

We have made an appointment with the {randAdj()} Dr. {sillyWord2}, who studied for many years in {place} and has {number} degrees in pediatrics. 

He will send you all the information you need. Thank you!
Sincerely
Mrs. {randAdj()}. ''')
