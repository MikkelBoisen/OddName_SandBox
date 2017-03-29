"""
write a program that asks the user for their name and has error-checking to make sure it's not blank.
Then print every second letter in the name. Hint: use a for loop, the range function, and the length of the name.
"""
def main():
    name = get_name()
    name_1 = name[1::2]
    print(name_1)


def get_name():
    name = input("Enter your name")
    if not name:
        print("You did not enter a name")
    else:
        print("Hello", name)
    return name


main()
