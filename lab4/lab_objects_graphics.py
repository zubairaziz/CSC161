"""CSC 161 Lab: Objects & Graphics

This programs draws a house after 5 clicks from the user.
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""

from graphics import *


def main():
    print("This programs draws a house after 5 clicks from the user.")
    win = GraphWin("5 click house.", 750, 750)
    win.setCoords(-750/2, -750/2, 750/2, 750/2)
    win.setBackground('white')
    message = Text(Point(0, 350), "Click 5 times.")
    message.draw(win)

    # Gets click from user to get the point for the bottom left
    # corner of the house
    message.setText("Click for bottom left corner of the house.")
    p1 = win.getMouse()
    p1.draw(win)

    # Gets click from user to get the point for the top right corner
    # of the house
    message.setText("Click for top right corner of the house")
    p2 = win.getMouse()
    p2.draw(win)

    # Draws the rectangle/square for the house based on the first two clicks
    house = Rectangle(p1, p2)
    house.setWidth(3)
    house.setFill('blue')
    house.draw(win)

    # calculates width of house and door
    houseWidth = abs(p2.getX() - p1.getX())
    doorWidth = (1/5 * houseWidth)

    # Gets click from user to get the point for the top edge of the door
    message.setText("Click inside the house for the top of the door.")
    p3 = win.getMouse()
    p3.draw(win)

    # Draws the door
    x1 = p3.getX() - (1/2 * doorWidth)
    x2 = p3.getX() + (1/2 * doorWidth)
    y = p3.getY()
    doorBottom = Point(x1, p1.getY())
    doorTop = Point(x2, y)
    door = Rectangle(doorBottom, doorTop)
    door.setWidth(3)
    door.setFill('red')
    door.draw(win)

    # Gets Click from user to get center of the window
    message.setText("Click inside the house for the center of the window.")
    p4 = win.getMouse()
    windowWidth = (3/4 * doorWidth)
    windowBottom = Point((p4.getX() - (windowWidth/2)),
                         p4.getY() - (windowWidth/2))
    windowTop = Point((p4.getX() + (windowWidth/2)),
                      p4.getY() + (windowWidth/2))

    # Draws the window
    window = Rectangle(windowBottom, windowTop)
    window.setWidth(3)
    window.setFill('cyan')
    window.draw(win)

    # Gets click from the user to click to get the top of the roof
    message.setText("Click above the house for the top ofc the roof.")
    p5 = win.getMouse()
    p5.draw(win)

    # Draws the roof
    p6 = Point(p1.getX(), p2.getY())
    roof = Polygon(p2, p5, p6)
    roof.setWidth(3)
    roof.setFill('yellow')
    roof.draw(win)

    # Quits on click
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
