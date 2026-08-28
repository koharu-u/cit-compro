n = int( input("n = ") )
A = []
for j in range(0,n) :
    print(j+1,"= ",end='')
    v = int( input( ) )
    A.append(v)

p = 0
for j in range(len(A)):
    if p < A[j]:
        p = A[j]
p = A.index(p)
print("the index of the maximum value list A = ", p)
