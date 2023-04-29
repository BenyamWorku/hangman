while True:
    guess=input("enter a letter of the alphabet.")
    if guess.isalpha() and len(guess)==1:
        break
    else:
        print("Invalid letter. \
              Please, enter a single alphabetical character.")