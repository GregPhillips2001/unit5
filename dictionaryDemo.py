#Greg Phillips
#11/15/17
#dictionaryDemo.py - list practice

dictionary = ["alphabet","sweatshirt","sweatpants","shorts","computer","waterbottle"]

dictionary.sort()

num = int(input("what number word do you want to look up? "))
if num >len(dictionary):
    print("Invalid")
else:
    print("Word number", num, "is", dictionary[num-1])
