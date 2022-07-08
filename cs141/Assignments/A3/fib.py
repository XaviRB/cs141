#Xavier Rodriguez
#Oct 22, 2019
#Description - fib and golden ratio

import sys

fib = int(sys.argv[1])# first input argument
#stating var
n = fib
a = 0
b = 1
# if n is 1 it prits inf
if n==1:
    print("infinity")
elif n == 2:# if its 2 then it prints 1
    print("1")
else:
    for i in range(1,n):# counting 
        c = a + b
        a = b
        b = c
        fib = b
    #this is to get the golden ratio but it brakes and its barely off
    gold = n/(n-1)
print("Fib:",fib,"Golden:", gold )# prints everything