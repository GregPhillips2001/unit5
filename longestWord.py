#Greg Phillips
#11/15/17
#longestWord.py

words = input("Enter words: ").split(" ")

l = 0
word = ""
for w in words:
    length = len(w)
    if length > l:
        l = length
        word = w
print("The longest word is", word)

    



