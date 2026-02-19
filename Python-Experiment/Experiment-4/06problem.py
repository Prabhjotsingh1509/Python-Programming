# Program to count number of unique words in a given sentence using sets. 

str= input("Enter the string:")

words=str.split()

uniqueWords=set(words)
print("The number of unique words:",len(uniqueWords))