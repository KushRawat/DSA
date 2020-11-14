def maxPairwiseNaive(digits, n):

    product = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, digits[i] * digits[j])

    return product

n = int(input())
digits = [int(x) for x in input().split()]

print(maxPairwiseNaive(digits, n))