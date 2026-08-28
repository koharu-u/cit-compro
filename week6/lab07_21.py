n = int( input("n = ") )
A = []
for j in range(0,n) :
    print(j+1,"= ",end='')
    v = int( input( ) )
    A.append(v)
d = []
for e in A:
    if((e % 2) != 0):
        d.append(e)
print(d)
