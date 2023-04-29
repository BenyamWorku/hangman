import random
word_list=["avocado","bananas","apples","mangoes","papaya"]
word=random.choice(word_list)
print(word)
while True:
    guess=input("enter a letter of the alphabet.")
    if guess.isalpha() and len(guess)==1:
        if guess in word:
            print(f"yes {guess} is in the word {word}")
            break
        else :
            print(f"sorry {guess} is not in the {word}.Try again.")
    else:
        print("Invalid letter. \
              Please, enter a single alphabetical character.")
    
