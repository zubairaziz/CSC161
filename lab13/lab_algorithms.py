"""CSC 161 Lab: Algorithms

This lab demonstrates a recursive algorithm to get the sum of a list
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""


def sum_list(my_list):
    if (len(my_list) == 0):
        return 0
    else:
        return my_list[0] + sum_list(my_list[1:])


def main():
    my_list = [7, 5, 4, 27, 52, 42, 13, 17]
    print(sum_list(my_list))


if __name__ == "__main__":
    main()
