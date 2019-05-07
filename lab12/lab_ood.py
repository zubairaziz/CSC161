"""CSC 161 Lab: Object Oriented Design

This lab simulates an ATM with classes and object oriented design
Extra credit: I did the GUI thing for the atm. Check it out

Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""


from account import Account
from atm import ATM


def main():
    atm = ATM()
    atm.menu()


if __name__ == "__main__":
    main()
