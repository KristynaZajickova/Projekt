"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Kristýna Zajíčková
email: hrbatova.kristyna@gmail.com
discord: Kristýna Z.
"""
import re

oddelovac = "-" * 40

# uživatelé a jejich hesla

user_database = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password123", 
    "liz": "pass123"
    }

user = input("Enter username: ")
if not user in user_database.keys():
    print("Unregistered user, terminating the program...")
    quit()

password = input("Enter password: ")
print(oddelovac)
if password != user_database.get(user):
    print("Unregistered user, terminating the program...")
    quit()
       
else:
    print(f"Welcome to the app, {user}")
    print("We Have 3 texts to be analyzed ")
    print(oddelovac)


# výběr textu 
texty = {
    "1", 
    "2",
    "3"
}


text_číslo = input("Enter a number btw. 1 and 3 to select: ")

if not text_číslo in texty:
    print("Wrong number, terminating the program...")
    quit()

else:
     text_číslo in texty
     print(oddelovac)



# rozbor textu č. 1

text_1 = ('''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''')

rozdelovac_text1 = text_1.split()

punctuations = ",.-:!?;"

no_punct = ""

def remove_punct(text_1):
    for char in text_1:
        if char not in punctuations:
            no_punct = no_punct + char

#print(no_punct)

vycisteny_text1 = ('Situated', 'about', '10', 'miles', 'west', 'of', 'Kemmerer,', 'Fossil', 'Butte', 
'is', 'a', 'ruggedly', 'impressive', 'topographic', 'feature', 'that', 'rises', 
'sharply', 'some', '1000', 'feet', 'above', 'Twin', 'Creek', 'Valley', 'to', 'an',
'elevation', 'of', 'more', 'than', '7500', 'feet', 'above', 'sea', 'level.', 'The',
'butte', 'is', 'located', 'just', 'north', 'of', 'US', '30N', 'and', 'the', 'Union', 
'Pacific', 'Railroad,', 'which', 'traverse', 'the', 'valley.')

vysledky = []

def vycistene_vysledky(text_1):
    for slovo in vycisteny_text1:

        vysledky.append(slovo)

#print(vysledky)


#počet slov

spaces = text_1.count(" ")
tabs = text_1.count("\t")
newlines = text_1.count("\n")
word = spaces+tabs+newlines+1


if text_1 == "":
    print(0)

else:
    print(f"There are {word} words.")

first_letter = []
big_letters = []
cisla = []

#počet slov začínajících velkými písmeny

for slovo in vycisteny_text1:
    if slovo.istitle():
        first_letter.append(slovo)

print(f"There are {len(first_letter)} titlecasewords.")


#počet slov psaných velkými písmeny


for slovo in vycisteny_text1:
    if slovo.isupper():
        big_letters.append(slovo)
    
print(f"There are {len(big_letters)} uppercasewords.")

#počet slov psaných malými písmeny

for slovo in vycisteny_text1:
    if slovo.islower():
        first_letter.append(slovo)

print(f"There are {len(first_letter)} lowercasewords.")

#počet čísel

for number in text_1:
    if number.isnumeric():
        cisla.append(number)

print(f"There are {len(cisla)} numeric strings.")

# suma všech čísel v text

def find_sum(text_1):
    
    return sum(map(int, re.findall('\d+', text_1)))
 

print(f"The sum of all the numbers {find_sum(text_1)}")
print(oddelovac)

#četnost slov

words_length = dict()

for slovo in vycisteny_text1:
    slovo = len(slovo)
    if slovo not in words_length:
        words_length.setdefault(slovo,1)
    else:
        words_length[slovo] = words_length[slovo] + 1
        
print("OCCURENCES")
print(oddelovac)
#print(words_length)

my_dict_1 = {8: 3, 5: 11, 2: 9, 4: 11, 9: 3, 6: 3, 1: 1, 10: 1, 11: 1, 7: 5, 3: 6}
for delka in my_dict_1:
    print('*'*my_dict_1[delka])

# rozbor textu č. 2

text_2 = ('''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''')


rozdelovac_text2 = text_2.split()

punctuations = ",.-:!?;"

no_punct = ""

def remove_punct(text_2):
    for char in text_2:
        if char not in punctuations:
            no_punct = no_punct + char

#print(no_punct)

vycisteny_text2 = ('At', 'the', 'base', 'of', 'Fossil', 'Butte', 'are', 'the', 'bright',
                'red,', 'purple,', 'yellow', 'and', 'gray', 'beds', 'of', 'the', 'Wasatch',
                'Formation.', 'Eroded', 'portions', 'of', 'these', 'horizontal', 
                'beds', 'slope', 'gradually', 'upward', 'from', 'the', 'valley', 'floor',
                'and', 'steepen', 'abruptly.', 'Overlying', 'them', 'and', 'extending',
                'to', 'the', 'top', 'of', 'the', 'butte', 'are', 'the', 'much', 'steeper',
                'buff-to-white', 'beds', 'of', 'the', 'Green', 'River', 'Formation,', 
                'which', 'are', 'about', '300', 'feet', 'thick.')

vysledky = []

def vycistene_vysledky(text_2):
    for slovo in vycisteny_text2:

        vysledky.append(slovo)

#print(vysledky)


#počet slov

spaces = text_2.count(" ")
tabs = text_2.count("\t")
newlines = text_2.count("\n")
word = spaces+tabs+newlines+1


if text_2 == "":
    print(0)

else:
    print(f"There are {word} words.")

first_letter_2 = []
big_letters_2 = []
cisla_2 = []

#počet slov začínajících velkými písmeny

for slovo in vycisteny_text2:
     if slovo.istitle():
          first_letter_2.append(slovo)

print(f"There are {len(first_letter_2)} titlecasewords.")


#počet slov psaných velkými písmeny

for slovo in vycisteny_text2:
     if slovo.isupper():
          big_letters_2.append(slovo)
    
print(f"There are {len(big_letters_2)} uppercasewords.")

#počet slov psaných malými písmeny

for slovo in vycisteny_text2:
    if slovo.islower():
        first_letter_2.append(slovo)

print(f"There are {len(first_letter_2)} lowercasewords.")

#počet čísel

for number in text_2:
    if number.isnumeric():
        cisla_2.append(number)

print(f"There are {len(cisla_2)} numeric strings.")

# suma všech čísel v text

def find_sum(text_2):
    
    return sum(map(int, re.findall('\d+', text_2)))
 

print(f"The sum of all the numbers {find_sum(text_2)}")
print(oddelovac)

#četnost slov

words_length = dict()

for slovo in vycisteny_text2:
    slovo = len(slovo)
    if slovo not in words_length:
        words_length.setdefault(slovo,1)
    else:
        words_length[slovo] = words_length[slovo] + 1

print("OCCURENCES")
print(oddelovac)
#print(words_length)

my_dict_2 = {2: 7, 3: 16, 4: 10, 6: 7, 5: 9, 7: 4, 10: 3, 8: 1, 9: 4, 13: 1}
for delka in my_dict_2:
    print('*'*my_dict_2[delka])

# rozbor textu č. 3

text_3 = ('''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''')


rozdelovac_text3 = text_3.split()

punctuations = ",.-:!?;"

no_punct = ""

def remove_punct(text_3):
    for char in text_3:
        if char not in punctuations:
            no_punct = no_punct + char

#print(no_punct)

vycisteny_text3 = ('The', 'monument', 'contains', '8198', 'acres', 'and', 'protects', 'a', 
                'portion', 'of', 'the', 'largest', 'deposit', 'of', 'freshwater', 'fish', 
                'fossils', 'in', 'the', 'world.', 'The', 'richest', 'fossil', 'fish', 'deposits',
                'are', 'found', 'in', 'multiple', 'limestone', 'layers,', 'which', 'lie', 
                'some', '100', 'feet', 'below', 'the', 'top', 'of', 'the', 'butte.', 'The',
                'fossils', 'represent', 'several', 'varieties', 'of', 'perch,', 'as', 'well', 
                'as', 'other', 'freshwater', 'genera', 'and', 'herring', 'similar', 'to', 'those', 
                'in', 'modern', 'oceans.', 'Other', 'fish', 'such', 'as', 'paddlefish,', 'garpike', 
                'and', 'stingray', 'are', 'also', 'present.')

vysledky = []

def vycistene_vysledky(text_3):
    for slovo in vycisteny_text3:

        vysledky.append(slovo)

#print(vysledky)


#počet slov

spaces = text_3.count(" ")
tabs = text_3.count("\t")
newlines = text_3.count("\n")
word = spaces+tabs+newlines+1


if text_3 == "":
    print(0)

else:
    print(f"There are {word} words.")

first_letter_3 = []
big_letters_3 = []
cisla_3 = []

#počet slov začínajících velkými písmeny

for slovo in vycisteny_text3:
     if slovo.istitle():
          first_letter_3.append(slovo)

print(f"There are {len(first_letter_3)} titlecasewords.")


#počet slov psaných velkými písmeny

for slovo in vycisteny_text3:
     if slovo.isupper():
          big_letters.append(slovo)
    
print(f"There are {len(big_letters_3)} uppercasewords.")

#počet slov psaných malými písmeny

for slovo in vycisteny_text3:
    if slovo.islower():
        first_letter_3.append(slovo)

print(f"There are {len(first_letter_3)} lowercasewords.")

#počet čísel

for number in text_3:
    if number.isnumeric():
        cisla_3.append(number)

print(f"There are {len(cisla_3)} numeric strings.")


# suma všech čísel v text

def find_sum(text_3):
    
    return sum(map(int, re.findall('\d+', text_3)))
 

print(f"The sum of all the numbers {find_sum(text_3)}")
print(oddelovac)

#četnost slov

words_length = dict()

for slovo in vycisteny_text3:
    slovo = len(slovo)
    if slovo not in words_length:
        words_length.setdefault(slovo,1)
    else:
        words_length[slovo] = words_length[slovo] + 1

print("OCCURENCES")
print(oddelovac)
#print(words_length)

my_dict_3 = {3: 15, 8: 7, 4: 9, 5: 7, 1: 1, 7: 12, 2: 11, 10: 2, 
6: 6, 9: 3, 11: 1}

for delka in my_dict_3:
    print('*'*my_dict_3[delka])