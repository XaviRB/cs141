# Author:Xavier Rodriguez
# Date: 11.10.19
# Description:sierpinski triangle 

#all imports
import turtle
import math
import random 
#window set up
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255

    t.up() # lift the pen
    #t.hideturtle() # hide the turtle triangle
    #screen.tracer(0, 0) # turn off redrawing after each movement
    return t

# finding the midpoint (given)
def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my

#the new function
def distance(x1, x2, y1, y2):
    """this is used to find the distnace between the two points which also helps with
        finding the color in the trinalges"""
    a = x2 - x2
    b = y2 - y1
    c = math.sqrt(a**2 + b**2)
    return c
#colors in the pixel
def color(point, canv_width, canv_height):
    """FIRST this function finds the canv_width divided by 255 and does the same for the height
        to find the pixel differnce between each other resulting in the new pixel width and pixel height.
        RGB is foundby subtracting 255 by the distance of the conner and divided by the width and height"""
    
    pixel_width = canv_width / 255
    pixel_height = canv_height / 255
    #RGB
    red = 255 - (distance(0, canv_height, 0, point[1]) / pixel_height)
    green = 255 - (distance(0, 0, point[0], 0) / pixel_width)
    blue = 255 - (distance(canv_width, 0, point[0], 0) / pixel_width)

    RGB = (int(red), int(green), int(blue))
    
    return RGB
#random point
def random_point(width, height):
    """This finds the random point within the canvas and gets a random x and y cordinate"""
    x = random.randint(0, width)
    y = random.randint(0, height)

    point = (x,y)
    return point

if __name__ == "__main__": 
    import sys
    import turtle
    
    # width and height are given as command line arguments:
    canv_width = int(500)
    canv_height = int(500)
    # Start by calling the turtle_setup function.
    t = turtle_setup(canv_width, canv_height)
    
    turtle.tracer(0,0)
    
    #chaos game
    #this gets a random point on the canvas
    point = random_point(canv_width, canv_height)
    
    #this gets the top of the triangle, 2nd one gets the right angle and the 3rd one gets the bottom left
    top = (midpoint((0, canv_height), (canv_width, canv_height)))
    right = (canv_width, 0)
    left = (0,0)
    #i got all of the angles together so when i call it to get c i can just call it.
    c_angles = (top,right,left)
    #pseudocode
    for i in range(100000):
       c = random.choice(c_angles) #this chooses a random angle and puts it in c
       m = midpoint(point, c) #the mid point between p and c
       
       t.penup()
        # Makes the turtle move to a random point within the canvas
       t.setpos(point)
       t.pendown()
       # Turtle draws a dot on its current position on the canvas 
       t.dot(2, color(point, canv_width, canv_height))
        
       point = m
    turtle.update()
    
    turtle.done()
#i cant get green to work i dont know why. i have adjusted everything with the color trying to
    #make it fill in but thats the only thing missing
    
    

    