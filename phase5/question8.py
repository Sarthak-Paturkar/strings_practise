##Take a string and count the number of  letters, lowercase letters, digits and special characters.
a=input()
upper=0
lower=0
digits=0
special=0
for i in a:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digits+=1
    else:
        special+=1

print(upper)
print(lower)
print(digits)
print(special)
