A = [4,7,2,8,5]

def findVal(a) : 
    s = 0
    for e in a :
        s = s + e*e
    return s

v = findVal(A)
print(“v = ”, v) 
