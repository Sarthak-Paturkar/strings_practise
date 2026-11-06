##Character frequency: Take a string and display the frequency of every character,
#ignoring spaces and case differences
a = input("Enter a string: ")
a = a.lower()
b = ""

for i in a:
    if i != " " and i not in b:
        print(f"{i} : {a.count(i)}")
        b+=i