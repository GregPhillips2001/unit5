#Greg Phillips
#12/4/17
#quiz5.py

#rand5
def rand5():
    from random import randint
    return([randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100)])
print(rand5())

#lastElement
def lastElement(A):
    return (A[-1])
print(lastElement(['dog','cat','rat']))

#biggest
def biggest(B):
    B.sort()
    return (B[-1])
print(biggest([3,-1,5,-2,7,2,1]))