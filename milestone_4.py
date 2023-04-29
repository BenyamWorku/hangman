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
        pass
