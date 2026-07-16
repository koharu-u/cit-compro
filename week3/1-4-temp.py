temp = eval(input("Enter the temperaure: "))
print(temp, "degree Celsius is ", end="")
if (30 < temp):
    print("Hot")
elif(20 < temp and temp <= 30):
    print("Warm")
elif(10 < temp and temp <= 20):
    print("Fine")
elif(temp < 10):
     print("Cold")
