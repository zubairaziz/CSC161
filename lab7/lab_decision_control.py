"""CSC 161 Lab: Decision Control

This program accepts a date in the form month/day/year and outputs \
    whether or not the date is valid
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""


def isLeapYear(year):
    # Check if a certain year is a leap year
    if (year % 4 != 0):
        return False
    elif (year % 100 == 0):
        if (year % 400 == 0):
            return True
        else:
            returnFals
    else:
        return True


# Function for checking the date
def validateInput(string):
    dateArr = string.split('/', 2)
    date = []

    for i in dateArr:
        date.append(int(i))

    # Date not less than 0
    if (date[0] <= 0 or date[1] <= 0 or date[2] <= 0):
        return False
    # Month not more than 13, Day not more than 32
    elif (date[0] >= 13 or date[1] >= 32):
        return False
    # Check date for each month
    elif (date[0] == 1 or date[0] == 3 or date[0] == 5 or date[0] == 7 or
          date[0] == 8 or date[0] == 10 or date[0] == 12):
        if (date[1] >= 32):
            return False
    elif (date[0] == 4 or date[0] == 6 or date[0] == 9 or date[0] == 11):
        if (date[1] > 30):
            return False
    # Check for leap year
    elif (date[0] == 2 and isLeapYear(date[2])):
        if (date[1] > 29):
            return False
    elif (date[0] == 2 and not(isLeapYear(date[2]))):
        if (date[1] > 28):
            return False
    return True


def main():
    print("This program accepts a date in the form month/day/year and outputs \
        whether or not the date is valid")
    dateString = (input("Please enter a date (mm/dd/yyyy): "))
    # Extra Credit - wrapped my function in try and except statements to cath
    # Value and Index errors
    # This is so that an error message prints when the user inputs date in an
    # invalid format
    try:
        if(validateInput(dateString)):
            print("%s is valid" % (dateString))
        else:
            print("%s is not valid" % (dateString))
    except (ValueError, IndexError) as err:
        print("Error: %s\nPlease try again.\n\n" % (err))
        main()


if __name__ == '__main__':
    main()
