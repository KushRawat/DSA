def moneyChange(money):
    
    coins = 0
    
    while money != 0:
        
        if money >= 10:
            money -= 10
            coins += 1

        elif money >= 5:
            money -= 5
            coins += 1

        else:
            money -= 1
            coins += 1

    return coins

x = int(input())
print(moneyChange(x))