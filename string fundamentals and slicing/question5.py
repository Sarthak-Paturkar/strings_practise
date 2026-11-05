'''
Palindrome using slicing: Check whether a 
given string is a palindrome using slicing.
 Ignore case differences.
'''
a=input("give a string: ")
up_a=a.lower()
if up_a[::]==up_a[::-1]:
    print("Yes!!!It's a palindrome")
else:
    print("NOO")