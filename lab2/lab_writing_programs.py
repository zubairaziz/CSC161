# File: lab_writing_programs.py
# A simple program that takes an expression from the user and evaluates it.
# Lab Section: MW 6:15PM - 7:30PM


def main():
    print("This program takes an expression from the user and evaluates it")
    # Extra credit - take input from user for how many time to run
    n = eval(input("How many calculations would you like to evaluate? "))
    # Loops through value "n" and assign mathematical expressions to variable x
    for i in range(n):
        x = input("Enter a mathematical expression: ")
        # Evaluates the given expression
        y = str(eval(x))
        print("%s = %s" % (x, y))
    print("Thank you for using this calculator :D")


main()
