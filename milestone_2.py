import random
word_list=["avocado","bananas","apples","mangoes","papaya"]
word=random.choice(word_list)
guess=input("Enter a single letter.")
if guess.isalpha() and len(guess)==1 :
    print("Good guess")
else:
    print("Oops,That isn't a valid input")
print(word)
