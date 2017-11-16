#Greg Phillips
#11/16/17
#warmup13.py

from random import randint

num = []
i = 1
while i<21:
    num.append(randint(0,50))
    i+=1
print("Min:",min(num))
print("Max:",max(num))
print("Sum:",sum(num))
    
