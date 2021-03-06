#greg phillips
#11/27/17
#cocktailsort.py - implementation of cocktail sort

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(A):
    i = 1
    while i < len(A):
        j=i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j] #swap in python
            j -= 1
        i += 1
    
    return A

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
