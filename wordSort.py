#Greg Phillips
#11/13/17
#wordSort.py

words = input("Enter words: ").split(" ") #.split(" ") recogmizes spaces and splits them into lists
words.sort()
for w in words:
    print(w)

