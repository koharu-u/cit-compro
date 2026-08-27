s = input("Base 2 : ")
l_base2 = len(s) - 1
while(l_base2 >= 0):
    if (not(s[l_base2] == "1" or s[l_base2] == "0")):
        print("Enter number 0,1 only.")
        exit()
    l_base2 -= 1
l_base2 = len(s) - 1
cnt,result = 0,0
while(l_base2 >= 0):
      result += int(s[cnt])*(2**l_base2)
      cnt += 1
      l_base2 -= 1
print("Base 10 :", result)
