#Greg Phillips
#11/13/17
#middleword.py

words = input("Enter words: ").split(" ") #.split(" ") recogmizes spaces and splits them into lists
num = len(words[:])

middle = num/2

if middle%2 == 0:
    print(words[middle-1], words[middle])
else:
        print(words[middle])

