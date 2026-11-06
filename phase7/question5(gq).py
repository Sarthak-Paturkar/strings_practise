'''
Username generator: Take a person's first name, last name and birth year. Generate a username using:
First three letters of the first name.
First three letters of the last name.
Last two digits of the birth year.

'''
a=input("Enter the first name of user: ")
b=input("Enter the last name of user: ")
c=input("Enter the birth year of the user: ")
a=a[:3]
b=b[:3]
c=c[-2:]
print(f"The username of the user is {a}{b}{c}")