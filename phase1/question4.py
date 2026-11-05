'''Remove first and last characters: Given a 
 string, print everything 
 except its first and last characters.'''

a=input("Give a string: ")
first_letter=a[1]
last_letter=a[-1]
print(first_letter)
print(last_letter)
print(a[1:len(a)-1:1])