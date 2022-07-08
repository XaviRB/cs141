# Author: Xavier Rodriguez
# Date: Dec 3, 2019
# Description: gets data and marks it on a picture to show earthquake data

import turtle

# copied from my lab 5 solution:
def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle's orientation and up/down state is the
        same as before.
    """
    # save the current pen state
    pen_was_down = t.isdown()
    
    # pick up pen, move to coordinates
    t.up()
    t.goto(x, y)
    
    # restore pen state
    if pen_was_down:
        t.down()

# copied from A4, with a couple slight modifications:
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle; return a turtle object in hidden
        state. The canvas has size canv_width by canv_height, with a
        coordinate system where (0,0) is in the center, and automatic
        re-drawing of the canvas is disabled. Set the background image to
        earth.png.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()
   
    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement
    
    turtle.bgpic('earth.png') # set the background image
    turtle.update()
    return t

def parse_row(line):
    """ Parse a line of the csv file, returning a dict with keys
    for latitude, longitude, timestamp, and magnitude.
    Pre: line is an unprocessed string representing a line of the file.
    Post: the returned dict has the following keys with values according
          to the data in the given line of the file:
            "latitude" -> (float)
            "longitude" -> (float)
            "timestamp" -> (str)
            "magnitude" -> (float)
    """
    # split the line into its constituent numbers
    lists = line.strip().split(",")
    # create a dictionary and populate it with the given keys
    data = {}
    
    data["latitude"] = float(lists[0])
    data["longitude"] = float(lists[1])  
    data["timestamp"] = str(lists[2])
    data["magnitude"] = float(lists[3])
    
    # return the resulting dictionary
    return data
def main():
    """ Main function: plot a circle on a map for each earthquake """
    # we'll scale coordinates and canvas to be 720x360, double
    # the size of the range of lat/lon coordinates
    scale = 2.0
    
    # call turtle_setup to set up the canvas and get a turtle
    t = turtle_setup(scale * 360, scale * 180)
    
    # open earthquakes.csv for reading
    file = open("earthquakes.csv", "r")
    
    
    # list for the earthquakes data 
    list_earthquakes = []
    
    # parse each line of the file using parse_row and adds each returned
    # dictionary into a list (skip the headers on the first line!) 
    for i in file.readlines()[1:]: # skips first line of data        
        list_earthquakes.append( parse_row(i))
    
    # for each earthquake dictionary in the list:
    for dictionary in list_earthquakes:
    # if the magnitude is larger than 1.0:    
        if dictionary["magnitude"] > 1.0:
            # teleport the turtle at coordinates (longitude * scale, latitude * scale).
            teleport(t, dictionary["longitude"] * scale, dictionary["latitude"] * scale)
            t.color("red")#red color for the circle
            t.circle(dictionary["magnitude"])# makes a cirlce for magnitude

    # turtle updated
    turtle.update()   
        
        
            

if __name__ == "__main__":
    main()

