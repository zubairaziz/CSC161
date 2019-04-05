"""CSC 161 Lab: Simulation & Design

This program runs a simulation of a two dimensional random walk
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019

Extra credit:
- Used graphics.py to visualize 2d walk
"""

import random
import math
from time import sleep
from graphics import GraphWin, Circle, Point, Line

# Extr credit - graphics window
SIZE = 800
win = GraphWin('2D Walk', SIZE, SIZE)
win.setBackground('white')
for i in range(SIZE):
    if (i % 20 == 0 and i > 0):
        for j in range(SIZE):
            if (j % 20 == 0 and j > 0):
                Point(i, j).draw(win)


def random_walk_2d(steps):
    distance = 0.00
    x = 0
    y = 0
    dir = ['left', 'right', 'forward', 'backward']
    # Extra credit - Visualization with graphics.py
    origin = Point(400, 400)
    c = Circle(origin, 3)
    c.draw(win)
    colors = ['black', 'purple', 'blue', 'red', 'green', 'brown']
    color = random.choice(colors)
    c.setOutline(color)
    c.setFill(color)
    for i in range(steps):
        direction = random.choice(dir)
        x_move = 0
        y_move = 0
        if (direction == 'left'):
            x -= 1
            x_move = -20
        elif (direction == 'right'):
            x += 1
            x_move = 20
        elif (direction == 'backward'):
            y -= 1
            y_move = -20
        elif(direction == 'forward'):
            y += 1
            y_move = 20
        new_coords = Point(origin.getX()+x_move, origin.getY()+y_move)
        line = Line(origin, new_coords)
        line.setOutline(color)
        line.draw(win)
        c.move(x_move, y_move)
        origin = new_coords
        sleep(0.15)
    distance = math.sqrt((x**2)+(y**2))
    return distance


def main():
    print("Simulation of two dimensional random walk")
    walks = eval(input("How many walks should I do? "))
    steps = eval(input("How many steps should I take on each? "))
    total_distance = 0
    average_distance = 0
    for i in range(walks):
        total_distance += (random_walk_2d(steps))
    average_distance = (total_distance)/walks
    print("Average distance from start: {0:.2f}".format(average_distance))
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
