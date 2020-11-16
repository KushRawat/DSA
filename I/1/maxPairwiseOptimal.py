def maxPairwiseOptimal(digits):
    
    digits.sort()
    return digits[-1] * digits[-2]

n = int(input())
digits = [int(x) for x in input().split('-')]

print(maxPairwiseOptimal(digits))