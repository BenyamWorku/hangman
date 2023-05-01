import random

class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word_list=word_list
        self.word=random.choice(self.word_list)
        self.word_guessed=['_']*len(self.word)
        self.num_lives=num_lives
        self.num_letters=len(set(self.word))
        self.list_of_guesses=[]
        #list_of_guesses- A list of the guesses that have already been tried. Set this to an empty list initially.
    
    def check_guess(self,guess):
      
       guess=guess.lower()
       if guess in self.word:
           print(f"Good guess! {guess} is in the word.")


    def ask_for_input(self):
        while True:
            guess=input(f"Guess a letter that you think is a part of the secret word {self.word}.")
            if not(guess.isalpha()) or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list=["avocado","bananas","apples","mangoes","papaya"]
game=Hangman(word_list,4)
game.ask_for_input()
