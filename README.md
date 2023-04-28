# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

#Milestone 1
Setup Github

#Milestone 2
This code fragment checks if the user's input is a single letter. It also generates random fruits from the list.
```
import random
word_list=["avocado","bananas","apples","mangoes","papaya"]
word=random.choice(word_list)
guess=input("Enter a single letter.")
if guess.isalpha() and len(guess)==1 :
    print("Good guess")
else:
    print("Oops,That isn't a valid input")
print(word)
```
