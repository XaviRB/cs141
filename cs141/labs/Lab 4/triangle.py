#Xavier Rodriguez
#0ct, 23, 2019
#Description -Triangle

def tri(width):
    for i in range (0,width):
        
        for j in range (0, i+1):
            print("*", end="")
         
        for k in range (width, 0,-1):
            print("*", end="")
        print()
    
width = 3
tri(width)
