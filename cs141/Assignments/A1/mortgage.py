#Auothor:Xavier Rodriguez
#Date:oct 7, 2019
#Description:Mortgage calculator

#price input
p = float(input("Home price (P):"))
#Down Payment input
d= float(input("Down Payment amount (D):"))
#monthly loan input
l= float(input("Loan term in months (N)"))
#rate input

r= float(input("Yearly intrest rate:"))
#intrest rate 
R=r*.01/12
# this would be the top of the equation
top = R*(1+R)**l
#this is the bottom of the equation 
bottom = ((1+R)**l) -1
#this is just combining everything together.
calculation = top/bottom * (p-d) 

#print to user
print("Monthly payment amount:",calculation)
