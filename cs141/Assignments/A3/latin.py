#Xavier Rodriguez
#Oct 22, 2019
#Description - latin squares
import sys
#importing the comand lines and creating names
numlength = int(sys.argv[1])
top_left_num = int(sys.argv[2])

#stating all the varibles and setting up new varibles used in the code later
numcount = 0# this is just creating a new count 
top_left_new_row = 0 # starting the new count row at 0 and going to add more later on in the code
top_left_new_row = top_left_num + top_left_new_row #setting the new row to be the same number that the user put in and count it 

if top_left_num > numlength: # just checking the condition if you put in a number in greater than the length 
    print("Top left number must be between 1 and side length")
else:
    for i in range (1,numlength):# this checks until the range of 1 to the number length
        while numcount != numlength:
            print(top_left_num, sep=" ", end=" ")# this gives the space between numbers
            #this adds the count by 1
            top_left_num = top_left_num + 1
            numcount = numcount + 1#this gets what number left in the line 
            #starts the line again and gets the number line when it finally
            if top_left_num == numlength + 1:
                top_left_num = 1
        print()#this prints the new row in the while loop 
        numcount = 0#part of creating a new row
        # adds one befoer starting the next row
        top_left_new_row = top_left_new_row + 1
        
        #this is the saftey net for when it reachest the the highest number adding one to numlength
        if top_left_new_row == numlength + 1:
            top_left_new_row = 1
            top_left_num = top_left_new_row
        else:
            top_left_num = top_left_new_row
