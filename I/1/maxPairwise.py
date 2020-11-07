# faster algorithm

n = int(input())

digits = [int(x) for x in input().split()]

index1 = 0
for i in range(1, n):
    if digits[i] > digits[index1]:
        index1 = i

if index1 == 0:         # handling descending digits 
    index2 = 1

for i in range(1, n):
    if digits[i] != digits[index1] and digits[i] > digits[index2]:
        index2 = i

print(digits[index1] * digits[index2])

    
