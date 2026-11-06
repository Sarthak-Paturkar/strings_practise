##Remove duplicate characters: Given a string, remove repeated characters while preserving the first occurrence.
a = input("Enter a string: ")
result = ""

for i in a:
    if i not in result:
        result += i

print(result)
