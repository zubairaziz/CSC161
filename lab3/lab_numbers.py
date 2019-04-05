# File: lab_numbers.py
# A simple program that implements Newton’s method.
# Lab Section: MW 6:15PM - 7:30PM


import math


def main():
    print("This program calculate the square root of a given number using the Newton's method")
    x = eval(
        input("What is the number for which you want to calculate the square root? "))
    n = eval(input("How many iterations do you want to use? "))
    y = x/2
    sqrt = math.sqrt(x)
    diff = y - sqrt
    # Extra Credit - Prints table showing the guess number and current estimate
    print("%d\t%f\t%f" % (1, y, diff))
    for i in range(n - 1):
        y = (y+(x/y))/2
        diff = y - sqrt
        print("%d\t%f\t%f" % (i + 2, y, diff))
    print("My guess for the square root of %d is %f" % (x, y))
    print("The difference between my guess and the real result is: %f" % (diff))


main()
