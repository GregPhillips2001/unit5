#greg phillips
#11/27/17
#cocktailsort.py - implementation of cocktail sort

from random import randint
from time import time

N = 100 #how many numbers will be sorted



def mySort(A):
    i = 0
    j = len(A)-1
    if A[i] > A[j]:
        A[i] = A[j]
    if (j-i+1) > 2:
        t = (j-i+1)/3
        mysort(A, i , j-t)
        mysort(A, i+t, j)
        mysort(A, i , j-t)
    
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
    
