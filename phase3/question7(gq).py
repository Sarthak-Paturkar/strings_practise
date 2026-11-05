##Take a sentence and replace multiple consecutive
#spaces with a single space. Do not use regular 
#expressions.
s = "Python    is   easy     to learn"

result = " ".join(s.split())

print(result)