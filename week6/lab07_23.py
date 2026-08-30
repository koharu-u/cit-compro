A = [45,10,12,9,99,13,11,65]
# j = 2 and k = 5 ➔sum = 133

j = int(input("j = ") )
k = int(input("k = ") )
sum = 0

for e in range(j,k+1):
    sum += A[e]
print("sum from",j,"to",k,"=",sum)
