"""CSC 161 Lab: Functions

This program computes the sum of the squares of numbers \
    read from a file.
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""


# Square each number in a list. Returns a new list with squared numbers

def square_each(nums):
    squared = []
    for i in nums:
        squared.append(i*i)
        i += 1
    return squared


# Calculates the sum of all numbers in a list
def sum_list(nums):
    j = 0
    for i in nums:
        j += i
    return j


# Converts strings to ints
def to_numbers(str_list):
    nums = []
    for i in str_list:
        nums.append(int(i))
    return nums


def main():
    print("This program computes the sum of the squares of numbers read from a \
        file.")
    filename = (input("Please enter the filename: "))
    str_list = []
    file = open(filename)
    line = file.readline()
    line = line.strip('\n')
    # extra credit - can split the string by either ',' or ' '
    line = line.replace(',', ' ')
    num = 0
    for i in range(len(line)):
        if (line[i] == ' '):
            num += 1
    str_list = line.split(' ', num)
    nums = to_numbers(str_list)
    nums = square_each(nums)
    nums = sum_list(nums)
    print(nums)


main()
