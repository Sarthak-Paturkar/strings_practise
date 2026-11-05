## Remove all occurrences of "Python" from a 
# sentence without considering uppercase or 
# lowercase differences. 
# Hint: Explore lower() and replace()
s = "I love Python. PYTHON is easy to learn. Python is powerful."

result = s.lower().replace("python", "")

print(result)