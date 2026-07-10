goods = int(input("Please enter price of goods: "))
banknote = int(input("Please enter money to pay: "))
change = banknote - goods

print("Money to change : ", change)
print("500 Baht :", (change // 500))
change %= 500
print("100 Baht :", (change // 100))
change %= 100
print("50 Baht :", (change // 50))
change %= 50
print("20 Baht :", (change // 20))
change %= 20
print("10 Baht :", (change // 10))
change %= 10
print("5 Baht :", (change // 5))
change %= 5
print("2 Baht :", (change // 2))
change %= 2
print("1 Baht :", (change // 1))
