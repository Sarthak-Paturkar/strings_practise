##Take a sentence and print the longest word. If multiple words have the same maximum length, print the first one.
a=input("Enter a string: ")
l=a.split()
longest=l[0]
for i in l:
    l_word=len(i)
    if l_word>len(longest):
        longest=i
print(longest)