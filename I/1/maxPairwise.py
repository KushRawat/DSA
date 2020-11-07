# faster algorithm

n = int(input())

digits = [int(x) for x in input().split()]

def MaxPairwiseProductFast(n, digits):

    index1 = 0
    for i in range(1, n):
        if digits[i] > digits[index1]:
            index1 = i

    if index1 == 0:         # handling descending digits 
        index2 = 1
    else:
        index2 = 0

    for i in range(1, n):
        if digits[i] != digits[index1] and digits[i] > digits[index2]:
            index2 = i

    return (digits[index1] * digits[index2])

print(MaxPairwiseProductFast(n, digits))        
