# Input a sentence and print words in seperate lines

s=input("Enter a string:")
words = s.split()

print("The words in the sentence are:")

for word in words:
    print(word)