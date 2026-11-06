## Vowel and consonant counter: 
# Count the vowels and consonants in a sentence. Ignore spaces, digits and special characters.
sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

for i in sentence:
    i = i.lower()  # Convert uppercase to lowercase

    if i.isalpha():  # Check whether it is an alphabet
        if i in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)