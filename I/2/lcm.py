def gcd(a, b):
    if b == 0:
        return a

    aR = a % b

    x = gcd(b, aR)     

    return x

def lcm(a, b):

    return ((a//gcd(a,b)) * b)

a, b = map(int, input().split())
print(lcm(a,b))