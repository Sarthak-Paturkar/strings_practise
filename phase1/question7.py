## Reverse every alternate character: Given a string, 
# extract characters at even indices and reverse
#that extracted string.

a=input("Enter a string: ")
extracted_string=a[0::2]
print(extracted_string[::-1])
