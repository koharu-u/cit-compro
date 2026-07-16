item1, item2, item3, item4 = eval(input("Product Price :"))
tot_p = item1+item2+item3+item4
print("Total Price =", tot_p)

# using if conditions for finding lowest price
if(item1 <= item2 and item1 <= item3 and item1 <= item4):
    print("Money to pay =", tot_p - item1)
elif(item2 <= item1 and item2 <= item1 and item2 <= item3):
    print("Money to pay =", tot_p - item2)
elif(item3 <= item1 and item3 <= item2 and item3 <= item4):
    print("Money to pay =", tot_p - item3)
elif(item4 <= item1 and item4 <= item2 and item4 <= item3):
    print("Money to pay =", tot_p - item4)

# using min() function for finding lowest price
# print("Money to pay =", tot_p - min(item1,item2,item3,item4))
