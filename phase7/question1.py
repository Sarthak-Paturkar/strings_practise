##Word frequency: Take a sentence and a word from the user.
#Count how many times that word occurs, ignoring case differences
a=input("Give me a sentence: ")
b=input("Give me a word: ")
l=a.lower().split()
b=b.lower()
count=0
for i in l:
    if i == b:
        count+=1
    else:
        pass
print(count)

