<!-- @format -->

# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

# Milestone 1

Setup Github

# Milestone 2

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

# Milestone 3

The two functions created are:
ask_for_input() and check_guess().
The former asks for input from the user and saves it into the guess variable .
It makes sure the input is just one letter.
The latter function checks whether the guessed letter is in the randomly generated word.
This function doesn't give the user the chance to pick another letter if they don't guess a letter from the word.

# Milestone 4

Created the Hangman class with attributes such as word_list, num_of_lives etc and two methods:

```class Hangman():
   def __init__(self, word_list, num_lives=5):
       self.word_list = word_list
       self.word = random.choice(self.word_list)
       self.word_guessed = ['_']*len(self.word)
       self.num_lives = num_lives
       self.num_letters = len(set(self.word))
       self.list_of_guesses = []
```

- **check_guess**: takes one argument 'guess' and determines if the guessed letter is in the secret word. If it isn't it notifies the user and shows how many tries are left.

```
def check_guess(self, guess):

       guess = guess.lower()
       if guess in self.word:
           print(f"Good guess! {guess} is in the word.")
           for i, _ in enumerate(self.word):
               if self.word[i] == guess:
                   self.word_guessed[i] = guess
           self.num_letters -= 1
       else:
           self.num_lives -= 1
           print(f"Sorry, {guess} is not in the word.")
           print(f"You have {self.num_lives} lives left.")
```

- **ask_for_input**: takes no argument. It prompts the user to enter one letter of the alphabet and validates the input.
  It informs the user if they have won or lost .

```
def ask_for_input(self):
       while True:
           guess = input(
               "Guess a letter that you think is a part of the secret word.")
           if not (guess.isalpha()) or len(guess) != 1:
               print("Invalid letter. Please, enter a single alphabetical character.")
           elif guess in self.list_of_guesses:
               print("You already tried that letter!")
           else:
               self.check_guess(guess)
               self.list_of_guesses.append(guess)
               if self.num_lives <= 0:
                   print(
                       "You have run out of lives before guessing the word correctly.Better luck next time.!")
                   break
               if '_' not in self.word_guessed:
                   print(f"You won! The word was {self.word}.")
                   break

```
