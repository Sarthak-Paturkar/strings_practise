##Take a sentence and join its words using " | " as a separator. Remove unnecessary leading and trailing spaces before processing.
a=input("Enter a string: ")
l=a.strip()
y=" | ".join(l.split())
print(y)
