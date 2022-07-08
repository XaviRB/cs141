#Author: Xavier Rodriguez
#Oct 13. 2019
#Description: Quadradic Formula Solver
import math
#This is asking for all the inputs from the user so i can use it in the quadratic equation
a = float(input("Please put in your a from your triniomial:"))
b = float(input("Please put in your b from your triniomial:"))
c = float(input("Please put in your c from your triniomial:"))

#this is saying that if the first cofficent is 0 then it's not a quadratic function
if a == 0:
    print("The a coffcient does not describe a quadratic!")

#this is just a peice of the puzzel from the quadratic equation 
rootthis = b**2 -4*(a*c)
#this is just checking if the first part is less than 0 then it would print out no real roots 
if rootthis < 0:
    print("No real roots")
else:
    quadraticpos = (-b + math.sqrt(rootthis))/ (2*a)#this is the postive part of the equation 
    quadraticneg = (-b - math.sqrt(rootthis))/ (2*a)#this is the negative part of the equation
    
    print(quadraticpos, quadraticneg)#printing out the pos and neg quadratic equation
