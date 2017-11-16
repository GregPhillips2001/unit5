#Greg Phillips
#11/16/17
#stringListDemo.py

words = input("Enter words: ").split(" ")

for w in words:
    if w[0] in "aeiouAEIOU":
        print(w)
