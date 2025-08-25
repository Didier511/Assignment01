#Task4.Assignment: while loop
#Display String Characters One By One, and their index

userWord=input("Enter a word: ")
index=0
while index<len(userWord):
    for Word in userWord:
        print(f"{Word}[{index}]")
        index+=1

