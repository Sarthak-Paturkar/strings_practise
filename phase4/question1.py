##Take a sentence and count the total number of words using split()
a = input("Enter a sentence: ")
count = 0

L = a.split()

for i in range(len(L)):
    count += 1

print("Total words:", count)