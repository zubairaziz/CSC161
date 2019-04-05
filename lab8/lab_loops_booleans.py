"""CSC 161 Lab: Decision Control

This program tests the Goldbach's conjecture
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019

Extra Credit:
- Reads a list of numbers from 'numbers.txt'
    'numbers.txt' is a file with one line of numbers separated by spaces
- Prints all possible combinations of prime numbers
"""


def get_input():
    accepted = False
    # While loop for checking if input is accepted
    while (not accepted):
        try:
            n = int(input("Enter an even number greater than 2: "))
            if ((n % 2 == 0) and (n > 2)):
                accepted = True
                return n
            else:
                print("Wrong Input!")
        except ValueError as error:
            print("Bad Input!")


def is_prime(n):
    if(n <= 3):
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    else:
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6
        return True


def get_file():
    try:
        file = open('numbers.txt', 'r')
        numbers = file.readline().split()
        return numbers
    except FileNotFoundError as error:
        print(error)
        exit()
    pass


def main():
    # The extra credit section will run immediately after the custom user input
    print("This program tests the Goldbach's conjecture")
    num = get_input()
    i = 1
    while(i <= num):
        j = num - i
        # Extra credit - Prints all possible combinations of prime numbers
        if(is_prime(i) and is_prime(j)):
            print("{0} = {1} + {2}".format(num, i, j))
        i += 1
    # Read numbers from file
    print('\nFor numbers in "numbers.txt": ')
    numbers = get_file()
    for i in range(len(numbers)):
        num = int(numbers[i])
        x = 1
        print('\n{0}: '.format(numbers[i]))
        while(x <= num):
            j = num - x
            if(is_prime(x) and is_prime(j)):
                print("{0} = {1} + {2}".format(num, x, j))
            x += 1


if __name__ == '__main__':
    main()
