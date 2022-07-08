# Author: Xavier Rodriguez
# Date:Nov, 18,19
# Description: This .py file genreates a pick and takes a user input to check if they win or not.

import random

def generate_winner(begin):
    """ Generate a winning lottery pick. If begin
        starts or ends with 1, 2, or 3, return that as the
        winning pick; othwerise, return a string
        containing one word (monkey, dragon, or snake)
        and one digit (1, 2, or 3) in either order. The
        random choices are made independently, so the chance
        of each possible pick is equal."""
    # Cheat code: if the user enters a string beginning or ending
    # with a digit when prompted to press enter to continue, use
    # whatever they entered as the winning pick.  
    
    if len(begin) > 0 and (begin[0] in "123" or begin[-1] in "123"):
        return begin
    
    # Do not modify above this line - the easter egg will be used for grading.
    
    # Otherwise, choose the winning pick randomly:
    
    # (TASK 1)
    # Pick the random digit
    digit = random.choice(["1","2","3"])
    # Pick one of three words
    word = random.choice(["monkey", "snake", "dragon"])
    # Decide which order they go in
    order_random = random.randint(0,1)
    #This says if the random order gets 0 then it will be digit then word and the else statement does the other making it random
    if order_random == 0:
        order = digit + word
    else:
        order = word + digit
    order = str(order)
    # return the combined lottery pick as a string
    return order
 

def get_valid_guess():
    """ Prompt the user until they enter a pick that contains one of the
        words (dragon, monkey, snake), and either begins or ends with one
        of the numbers (1, 2, or 3). When a valid guess is entered, return
        it. """
    # (TASK 2)
    # while the user has not entered a valid pick:
    #    prompt the user for a pick
    #    check if it's valid (contains one of the words and one of the numbers)
    #    if not, print a message saying what's missing
    #    if it is, return the valid pick
    valid_guess = False
    while valid_guess is not True:# while false is not false it will keep the while loop going
        guess = input("Please enter your pick:")#gets the users input checking if its a valid guess first
         #   
        if "dragon" in guess or "snake" in guess or "monkey" in guess:#this checks the words if its in the input
            if "1" in guess or "2" in guess or "3" in guess:#this checks the digits between 1-3
                valid_guess = True #it will com back as true 
                return guess
            else:
                print("You dont have digit or you dont have a digit between 1-3")
        else:
            print("You dont have a word or one of the correct words ex.(snake, dragon, monkey)")
def check_string(string):
    """This gets the string and checks if the first part of the string is either a digit or a string.
        if its a digit first then it will return as true if it doesnt come back as true then it goes
        to else and makes it false."""
    if string[0].isdigit(): #this is a function isdigit() checks if theres a digit in the string for the first or last coming back with T or F
        digit = string[0] #saying that the digit is the first part of the string
        word = string[1:] #the end part is the word
        digit_first = True #comes back as true
    else:#if the first one is not true then it will come back false saying that the digit_first is not actually first but at the [-1]
        digit = string[-1] #this makes the digit at the end 
        word = string[:-1]#this makes the word on the first half
        digit_first = False #returns as false
        
    return digit, word, digit_first#returns 3 things so it is split

def main():
    """ Generate a lottery pick and check whether a user has guessed it
        correctly.  """
   
    welcome_message = """Welcome, and thanks for playing Lotter.io!
Let's see if you've won. Today's word choices are
monkey, dragon, and snake; the digit choices were
1, 2, and 3. The winning pick is a word and a digit,
in either order. Press enter to begin:"""
    
    print(welcome_message)
    begin_input = input() # enter to continue (or enter a cheat code!)

    # generate a winning lottery pick
    winning_pick = generate_winner(begin_input)

    # Get a valid guess from the user:
    guess = get_valid_guess()
    
    # (TASK 3)
    # determine the user's word and number choices, based on whether the
    # first or last characater is one of the numbers
    
    # check string gets the string and this returns the word the digit and if the digit is first
    # checks both the guess from user and the computers winning_pick and this will help define the print message 
    guess_digit, guess_word, guess_digit_first = check_string(guess)
    winning_digit, winning_word, winning_digit_first = check_string(winning_pick)
    
    #this takes the string and finds out if 
    
    # print a message for whichever of the following cases is applicable:
    #   - their pick matches character for character, therefore they win
    #   - the word and number are both correct but the pick doesn't match
    #   - the word is correct but the number is incorrect
    #   - the number is correct but the word is incorrect
    #   - all other cases: neither the word nor the number is correct
    
    #These if statements determine if the number or word or ordering is true or false.
    if winning_pick == guess:#   - their pick matches character for character, therefore they win
        print("congrats you guessed the right answer and you won the lotter.io")
    #   - the word and number are both correct but the pick doesn't match
    elif winning_digit == guess_digit and winning_word == guess_word and winning_digit_first != guess_digit_first:
        print("Yay, you got the digit and word correct but unfortnuatly the order is wrong.")
    #   - the word is correct but the number is incorrect
    elif winning_word == guess_word and winning_digit != guess_digit:
        print("Unfortunatly you have the correct word but you don't have the right digit.")
    #   - the number is correct but the word is incorrect
    elif winning_digit == guess_digit and winning_word != guess_word:
        print("You have the correct digit but unfortunatly you dont have the correcct word.")
    
    else:#   - all other cases: neither the word nor the number is correct
        print("You didn't get either right, try guessing a number and word again.")

        
if __name__ == "__main__":
    main()
