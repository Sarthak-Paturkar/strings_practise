##Reverse each word: Take a sentence and reverse every individual word without changing the order of the words.
a=input("Enter a sentence: ")
a=a.split()
for i in a:
    b=i[::-1]
    print(b,end=" ")