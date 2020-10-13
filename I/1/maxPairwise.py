n = int(input())
digits = [int(x) for x in input().split()]

product = 0

for i in range(n):
    for j in range(i + 1, n):
        product = max(product, digits[i] * digits[j])

print(product)