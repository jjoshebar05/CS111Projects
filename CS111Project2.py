#Joshua Ebarvia, CS111 Project 2 (9/19/24)

import random
random.seed(5) #Do not delete this line!!
artist_songs = { "Shaboozey":["A Bar Song (Tipsy)"] ,  "SabrinaCarpenter":["Taste","Please Please Please","Espresso"]  , "PostMalone": ["I Had Some Help","Pour Me A Drink", "Guy For That"] ,"BillieEilish" : ["Birds Of A Feather","Wildflower"] }

#Milestone 1 - Task 1: Ask the user for a command

commandOne = str(input("Enter command: "))

#Milestone 1 - Task 2: Split the command

spaceIndex = commandOne.find(" ")
firstWord = commandOne[0:spaceIndex]
secondWord = commandOne[spaceIndex+1:]

print("First word of the command is: " + firstWord + "\n" + "Second word of the command is: " + secondWord + "\n")

artistKeys = ["Shaboozey", "SabrinaCarpenter", "PostMalone", "BillieEilish"]

#Milestone 1 (Top Hit?) + 2 Code
if (firstWord == "Songs") and (secondWord in artistKeys):
    topHit = str(input("Tophit ? (yes/no): " ))
    artistKeys = artist_songs[secondWord]
    if (topHit == "yes"):
        print("My Song Choice: " + "\n" + artistKeys[0])
    elif (topHit == "no"):
        print("My Song Choice: ")
        print(artistKeys)
    #Milestone 4.2
    elif (topHit != "yes") and (topHit != "no"):
        print("Incorrect choice, should be \"yes\" or \"no\".")
#Milestone 4.1A
elif (firstWord == "Songs") and (secondWord not in artistKeys) and (secondWord != "AllHits"):
    print(f"Incorrect second command {secondWord}, should be \"AllHits\" or the Artist's Name instead.")

#Milestone 3
if (firstWord == "RandomSong") and (secondWord in artistKeys):
    artistKeys = artist_songs[secondWord]
    songLength = len(artistKeys)
    randSong = random.randint(0, songLength-1)
    print("My Song Choice: " + "\n" + artistKeys[randSong])
#Mileston 4.1B
elif (firstWord == "RandomSong") and (secondWord not in artistKeys) and (secondWord != "AllHits"):
    print(f"Incorrect second command {secondWord}, should be the Artist's Name instead.")

shaboozeySongs = artist_songs["Shaboozey"]
sabrinaSongs = artist_songs["SabrinaCarpenter"]
postSongs = artist_songs["PostMalone"]
billieSongs = artist_songs["BillieEilish"]
allSongs = [shaboozeySongs, sabrinaSongs, postSongs, billieSongs]

if (firstWord == "Songs") and (secondWord not in artistKeys) and (secondWord == "AllHits"):
    print("My Song Choice: ")
    print(allSongs)

#Milestone 4 - Task 3: Incorrect First Command

firstCommands = ["Songs", "RandomSong"]
if firstWord not in firstCommands:
    print(f"Incorrect first command {firstWord}, should be \"Songs\" or \"RandomSong\" instead.")