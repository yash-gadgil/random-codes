
from random import *
words = ("waddle", "shorthand", "quadriceps", "forklift", "bottlecap", "foreign", "conqueror", "geography", "controller", "twofold", "literature",
         "wanderer", "manifest", "cylinder", "shampoo", "ukelele", "ambrosia", "laminar", "equations", "salamander")
while True:
    p = input("\nDo you want to play Hangman? ")
    if p.lower() == "yes":
        word, guesses, l, c = choice(words), 6, "", 0      
        while True:
            if guesses == 0:
                print("Hangman completed! Try again")
                break
            for i in word:
                if i not in l:
                    print("_", end = " ")
                else:
                    print(i, end = " ")
                    c += 1
            if c == len(word):
                print("\nYou guessed the word!")
                break
            while True:
                letter = input("\nEnter guess letter: ")
                if letter not in l:
                    break
                else:
                    print("Already Guessed.")
            if letter not in word:
                guesses -= 1
                print("\nYou have",guesses,"guesses left.")
            l += letter
            c = 0
    else:
        break
