#Joshua Ebarvia, CS111 @ UIC, Project 1, September 15, 2024

#original word
print("-------- initial setup --------")
word = input("Enter a word: ")
# word = "COMPUTERS"

index1 = int(input("enter first index: "))
index2 = int(input("enter second index: "))
print("-------- end of setup --------\n")

# make variables to hold each of the 5 chunks (the first 3 are started for you)
# add code for the middle and using variables index1 and index2. Note: you
# may need to add 1 to some slice indexes to get the right slice
char1 = word[index1]
char2 = word[index2]
front = word[:index1]
middle = word[index1 + 1:index2]
back = word[index2 + 1:]

# concatentate the chunks together as shown in the diagram
scrambled_word = front + char2 + middle + char1 + back

# PRESENT GAME TO THE USER
print("Welcome to SWITCHEROO!")
print("Below is a word in which two of the letters have been switched.")
print("Can you guess which ones?")
print("")

#add code below here

indexes = "0123456789" #use to display index numbers to user
print(indexes[0:len(word)])
print(scrambled_word)
print("")

#FINAL PART CODE
#The word shown for "your guess" should swap the indexes of the scrambled word, not the original.

guessIndex1 = int(input("Enter the index of the FIRST character you think was swapped: "))
guessIndex2 = int(input("Enter the index of the SECOND character you think was swapped: \n"))

char1 = scrambled_word[guessIndex1]
char2 = scrambled_word[guessIndex2]
front = scrambled_word[:guessIndex1]
middle = scrambled_word[guessIndex1 + 1:guessIndex2]
back = scrambled_word[guessIndex2 + 1:]

result = front + char2 + middle + char1 + back

print("Your guess:" + result)
print("Secret word:" + word)
print("Did you get it right?")
