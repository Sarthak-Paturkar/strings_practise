'''
String validation: Create a program to validate a username:
Minimum 8 characters.
Must contain alphabets and digits.
Must not contain spaces.
Must not contain special characters.
'''
a = input("Enter a username: ")

has_alpha = False
has_digit = False

for i in a:
    if i.isalpha():
        has_alpha = True
    elif i.isdigit():
        has_digit = True

if len(a) >= 8 and has_alpha and has_digit and a.isalnum():
    print("Valid username")
else:
    print("Invalid username")