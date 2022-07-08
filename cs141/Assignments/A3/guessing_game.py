#Xavier Rodriguez
#oct 22 19
#Description, guessing game
import random
import sys
# getting all the var and defining the comand line
tries = int(sys.argv[1]) 
mode = sys.argv[2]
fixed = sys.argv[2]
#labeling what my var are for random and trying to label what my fixed answers would be
answer1 = random.choice("bellingham")
answer2 = random.choice("bellingham")
answer3 = mode
answer4 = fixed
# This is here to check if the answers are false
guess1 = False
guess2 = False

#this is story
print('Lets play a letter guessing game. the goal is for you to guess two letters chosen randomly from among the letters in the word "bellingham"'
        '. The two letters can be the same.')
# a counter to make sure the tries are counted properly 
maxtries = tries + 0

#PLAYER MODE
if tries >= 0 and mode == "PLAYER":
    if tries < 2: #cheking if they put an invalid number
        print("Your number of tries must be a number greater than 2")
    elif tries >=2 :#starting to run the function
        for i in range (1,maxtries+1):# this is a range counter to make sure everything is counted properly in tries
            print("==========================================")
            print("guess #", i)
            
            guess = input("please enter your guess:")# the first input from user 
            
            if guess == answer1 and answer2 == False:#checking if the first guess is correct
                print("you have sucssfully guessed the first letter.")
                guess1 = True
            elif guess != answer1 and guess1 == False:# if the guess is false it will say the guess is not correct
                print("The first letter is not,", guess)
                
            elif guess == answer2 and guess2 == False:# checking if the second input is correct or not
                print("You got the second letter")
                guess2 = True
            elif guess != answer2 and guess2 == False:# checking it if its false
                print("The second letter is not,", guess)
                
            elif guess1 == True and guess2 ==True:# printing this if everything is true
                print("Congrats, you guessed the secret letters", answer1, "and", answer2, "You won!!!")
            else:
                if i >= maxtries:#if mac tries are met then it prints game over
                    print("==========================================")
                    print("you have run out of tries. Game over.")
                    print("The secret letters were",answer1,"and", answer2,)
                    exit()
else:# DEBUG MODE

    for i in range (1,maxtries +1):
        print("==========================================")
        print("guess #", i)
        
        debug = fixed or mode # this is suposed to work because i set the values but its not working it only says one correct one
        
        if debug == answer3 and answer4 == False:#checking if the first guess is correct
            print("you have sucssfully guessed the first letter.")
            guess1 = True
        elif debug != answer3 and guess1 == False:# if the guess is false it will say the guess is not correct
            print("The first letter is not,", debug)
                
        elif debug == answer4 and guess2 == False:#printing this if its true
            print("You got the second letter")
            guess2 = True
        elif debug != answer3 and guess2 == False:#if it is not correct then it will print out this
            print("The second letter is not,", debug)
        
        elif guess1 == True and guess2 ==True:# printing out if the answer is correct
            print("Congrats, you guessed the secret letters", answer1, "and", answer2, "You won!!!")
    else: # if its false then it prints out game over
        if i >= maxtries:
            print("==========================================")
            print("you have run out of tries. Game over.")
            print("The secret letters were",answer1,"and", answer2,)
            exit()
            
                
                
                
                
                