#Author: Xavier Rodriguez
#Date: oct 9. 2019
#Description: Drinking age check
#this is just asking for the input of the user and is storing it in year
year = int(input("Enter your birth year (e.g., 1982):"))

#this is just asking for the input of the user and it is storing the month
month = int(input("Enter your birth month(e.g., 2 for february):"))

#the if statement is checking if the year is less than 1998 and checking if its true
if year < 1998:
    print("Hell yeah drink up!")
#this elif is just checking if the year is greater than 1998 then no booze
elif year > 1998:
    print("No booze for you!")
# this elif is checking if it is the even year then the month would have to be before 10 or octorber
elif year == 1998 and month < 10:
    print("Hell yeah drink up!")
#if none of them are true no booze for you
else:
    print("No booze for you!")


