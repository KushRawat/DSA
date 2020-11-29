def gcd(a, b):
    if b == 0:
        return a

    aR = a % b

    x = gcd(b, aR)     

    return x

a, b = map(int, input().split())
print(gcd(a, b))   
