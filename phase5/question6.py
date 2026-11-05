'''Take a string and classify it into one of these categories:
Only alphabets
Only digits
Alphanumeric
Contains special characters'''

a = input("Enter a string: ")

if a.isalpha():
    print("Only alphabets")

elif a.isdigit():
    print("Only digits")

elif a.isalnum():
    print("Alphanumeric")

else:
    print("Contains special characters")