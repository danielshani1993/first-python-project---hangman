from ast import If
from cmath import sqrt
import math
from inspect import CORO_SUSPENDED
from re import X
from tkinter import N
from xml.etree.ElementTree import PI


def game_addline():
    print("welcome to game Hangman")
    print( """
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _____
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' |  _  |
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/""")

def picture_1():
    print("x-------x")
    return None

def picture_2():
    print("x-------x\n")
    print("|\n")
    print("|\n")
    print("|\n")
    print("|\n")
    print("|\n")
    return None

def picture_3():
    print("x-------x\n")
    print("|       |\n")
    print("|       0\n")
    print("|\n")
    print("|\n")
    print("|\n")
    return None

def picture_4():
    print("x-------x\n")
    print("|       |\n")
    print("|       0\n")
    print("|       |\n")
    print("|\n")
    print("|\n")
    return None

def picture_5():
    print("x-------x\n")
    print("|       |\n")
    print("|       0\n")
    print("|      /|\ \n")
    print("|\n")
    print("|\n")
    return None

def picture_6():
    print("x-------x\n")
    print("|       |\n")
    print("|       0\n")
    print("|      /|\\\n")
    print("|      /\n")
    print("|\n")
    return None

def picture_7():
    print("x-------x\n")
    print("|       |\n")
    print("|       0\n")
    print("|      /|\\\n")
    print("|      / \\\n")
    print("|\n")
    return None

def letter_guess():
#letters in the word
    print("guess the letter:")
    letter = input()
    if (letter>='A'or letter<='Z'):
        letter = letter.lower()
    print("you guessed: " + letter)

def word_enter_guess(): #enter the word
#word in the game
    print("choose the word for the game: ")
    word = input()
    print("_ " * len(word))
    return word

def check_the_letter(let,word): #check the letter in the word
    if let in word:
        print("correct")
    elif(let.length() > 1):
        print("worng - E1")
    else:
        print("worng - E2")

def is_valid_input(let): #check the letter in the word
    if let.isalpha():
        return True
    else:
        return False
