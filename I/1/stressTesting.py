def maxPairwiseNaive(digits, n):

    product = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, digits[i] * digits[j])

    return product

def maxPairwiseOptimal(digits):
    
    digits.sort()
    return digits[-1] * digits[-2]

import random

def stressTest(N,M):
    
    while True:
        
        n = random.randint(2, N)
        print(n)
        array = []

        for i in range(0, n):
            r = random.randint(0,M)
            array[i] = r 

        print(array)

N = int(input())
M = int(input())
stressTest(N,M)