"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Olga Portesova
email: olikportesova@seznam.cz
"""

# import modulu regex a Counter z knihovny collections 
import re
from collections import Counter


# vytvoření proměnné s hlavním textem
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


# vyžádání si od uživatele přihlašovací jméno a heslo
username = input("username: ")
password = input("password: ")


# vytvoření proměnné registrovaných uživatelů
registered = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123",
}


# ověření přihlašovacích údajů (ukončení programu, pokud není registrovaný)
if username not in registered or registered[username] != password:
    print("unregistered user, terminating the program..")
    exit()

# pozdravení registrovaného uživatele
print("-" * 40)
print("Welcome to the app,", username)

# vypsání počtu textů k analyzování
print("We have", len(TEXTS), "texts to be analyzed.")
print("-" *40)


# výběr textu (ukončení programu, pokud uživatel zadá cokoliv jiného, než čísla)
text_choice = input("Enter a number btw. 1 and 3 to select: ")
if not text_choice.isdigit():
    print("The entered data is not a number, terminating the program..")
    exit()

# výběr textu (ukončení programu, pokud užvatel zadá jiná čísla než 1-3)
text_choice = int(text_choice)
if text_choice < 1 or text_choice > 3:
    print("The value must be between 1 - 3, terminating the program..")
    exit()


# vytvoření proměnné pro vybraný text
selected_text = TEXTS[text_choice - 1]


# vytvoření listu pro lepší pracování s textem (bez interpunkce)
words = [word for word in re.sub(r"[^a-zA-Z0-9]", " ", selected_text).split() if word]


# počítání statistik
word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper() and not word.isdigit())
lowercase_count = sum(1 for word in words if word.islower() and not word.isdigit())
numeric_count = sum(1 for word in words if word.isdigit())
numeric_sum = sum(int(word) for word in words if word.isdigit())


# vypsání statistik
print("-" * 40)
print("There are", word_count, "words in the selected text.")
print("There are", titlecase_count, "titlecase words.")
print("There are", uppercase_count, "uppercase words.")
print("There are", lowercase_count, "lowercase words.")
print("There are", numeric_count, "numeric strings.")
print("The sum of all the numbers", numeric_sum)
print("-" * 40)


# zjištění délek slov
word_lengths = Counter(len(word) for word in words)


# vytvoření sloupcového grafu
print("LEN|  OCCURRENCES  |NR.")
print("-" * 40)
for length in sorted(word_lengths.keys()):
    stars = "*" * word_lengths[length]
    print(f"{length:2} |{stars:<20} |{word_lengths[length]}")