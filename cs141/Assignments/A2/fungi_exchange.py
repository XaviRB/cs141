#Xavier Rodriguez
#0ct 15 2019
#Description: Fungi game

#this is just getting the users inputs and making it into an interger 
shiitakes = int(input("How many shiitakes have you picked up?"))
portabellos = int(input("How many portabellos have you picked up?"))
#The story just being printed out
print('As you meander through the forest, you round the corner and a soup chef appears out of nowhere and hits you over'
       'the head with a wooden spoon,"Watch where your going!" She says. She peers into your bag and her demeanor'
       'changes immediately."I have rubies I can give you for those mushrooms..."')
#this is just getting the users inputs and making it into an interger
shiitakes_trading = int(input("How many shiitakes are you willing to trade?"))
portabellos_trading = int(input("How many portabellos are you willing to trade?"))

#this is checking if the user is choosing to trade nothing
if shiitakes_trading + portabellos_trading == 0:
    print('The soup chef twitches and says, "If you dont want to trade, then get out of my woods!"')
    exit()
#this is checking if they are trying to input an number greater then the number they picked    
if shiitakes_trading > shiitakes or portabellos_trading > portabellos:
    print("The chef quickly woddles away")
    exit()
#this is checking if it is less than 10 and less than 5
if shiitakes_trading < 10 and portabellos_trading < 5:
    rubies = shiitakes * 2
#this is checking if it is less than 10 and greater or equal to 5
elif shiitakes_trading < 10 and portabellos_trading >= 5:
    rubies = portabellos_trading * 3
#this is checking for the multiples using the moduals and seeing if the remainder is 0 and if it is not a multiple of 24
elif shiitakes_trading % 12 == 0 and shiitakes_trading % 24 !=0 and portabellos_trading > 20:#this last part is checking if it is greater than 20
    rubies = portabellos_trading * 4
#this is checking for the multiples using the moduals and seeing if the remainder is 0 and if it is not a multiple of 24
elif shiitakes_trading % 12 == 0 and shiitakes_trading % 24 !=0 and portabellos_trading < 20:#lastpart is checking if it is less than 20
    rubies = portabellos_trading

else:# this is excuted if all of the others fail
    rubies = shiitakes * 5
    
print("The chef offers you", rubies, "rubies.")# printing out the offer


yes_no= input("Do you accept the trade? (Y/N)")#getting the users input and storing it

shiitakes_new = shiitakes - shiitakes_trading#the math to check if they traded
portabellos_new = portabellos - portabellos_trading#the math to check if they traded 

if yes_no == "yes" or yes_no =="Yes" or yes_no == "YES":#if yes then it excutes the code giving the total amount of everything
    print("You make the exchange, and walk away with", rubies, "rubies,",
          shiitakes_new, "shiitakes, and", portabellos_new, "portabellos.")
    exit()
else:#this gets excuted if they put anything other than yes this code gets excuted 
    print('The soup chef twitches and says, "If you dont want to trade, then get out of my woods!')
    exit()


