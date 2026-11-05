##Extract middle characters: Take a string from
#  the user and print its middle character if 
# its length is odd. 
# If even, print the two middle characters.

a = input("Enter a string: ")

if len(a) % 2 != 0:  # Odd length
    print(a[len(a) // 2])
else:  # Even length
    mid = len(a) // 2
    print(a[mid - 1 : mid + 1])