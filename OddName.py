"""
write a program that asks the user for their name and has error-checking to make sure it's not blank.
Then print every second letter in the name. Hint: use a for loop, the range function, and the length of the name.
"""

name = input("Enter your name")
print("Hello", name)
if not name:
    print("You did not enter a name")
else:
    print("Good job")
#did not do the for-loop
for name in range(1,6,2):
    print(name)