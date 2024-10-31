
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")


length1 = len(word1)
length2 = len(word2)


if length1 > length2:
    difference = length1 - length2
    print(f"The word '{word1}' has {difference} more letters than '{word2}'.")
elif length2 > length1:
    difference = length2 - length1
    print(f"The word '{word2}' has {difference} more letters than '{word1}'.")
else:
    print("The two words have the same length.")
