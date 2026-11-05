##Extract alternate characters: Print characters at even indices and odd indices 
a=str(input("Enter a string: "))
even_indices_elements=a[0:len(a)+1:2]
odd_indices_elements=a[1:len(a)+1:2]
print(even_indices_elements)
print(odd_indices_elements)
