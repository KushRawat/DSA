def moneyChange(money):

    coins = 0
    
    if money >= 10:
        coins = money // 10
        money = money % 10

    if money >= 5:
        coins += money // 5
        money = money % 5

    if money >= 1:
        coins += money // 1
    
    return coins

x = int(input())
print(moneyChange(x))