## Convert a given sentence into lowercase and 
# count how many characters changed.
a = input("Enter a sentence: ")
lower = a.lower()
count = 0
for i in range(len(a)):
    if a[i] != lower[i]:
        count += 1
print("Lowercase sentence:", lower)
print("Characters changed:", count)

