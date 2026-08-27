pwd = input("Enter Password: ")
cnum = 0
for num in pwd:
    if num.isdigit():
     cnum += 1
if (len(pwd) >= 8 and cnum >= 2 and pwd.isalnum()):
    print("password is vaild.")
else:
    print("password is invaild.")
