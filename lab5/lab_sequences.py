"""CSC 161 Lab: Sequences

his program reads in financial information from a file and prints \
    it neatly to the user's screen.
Zubair Ab Aziz
Lab Section MW 6:15pm-7:30pm
Spring 2019
"""


def main():
    print("This program reads in financial information from a file and prints \
        it neatly to the user's screen.\n")
    # Takes user input for filename and opens the file
    filename = (input("Please enter the filename of the financial data: "))
    data = []
    with open(filename, "r") as file:
        i = 0
        lines = file.readlines()
        # Inserts data into list
        for line in lines:
            if i > 2:
                data.insert(i, float(line.split('\n')[0]))
            else:
                data.insert(i, (line.split('\n')[0]))
            i += 1
    file.close()
    i = 0
    for lines in (data):
        if i < 3:
            data[i] = float(lines.split(' ')[1])
        i += 1

    # Prints out data in a table
    percent = "%"
    print("\nThe initial principal is: $%.2f" % (data[1]))
    print("Annual percentage rate is: %.1f%s" % ((data[2] * 100), percent))
    print("Length of term (years) is: %d\n" % (data[0]))

    print("Year\tValue")
    print("---------------")
    i = 0
    j = 0
    for lines in data:
        if i > 2:
            print("%d\t$%.2f" % (j, (data[i])))
            j += 1
        i += 1


main()
