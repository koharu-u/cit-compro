A = [[1,2,3,4],
     [5,6,7,8],
     [9,0,6,3]]

# ---- SNIP ----

A_t = []

for A_x in range(len(A[0])):
    A_t.append([])
    for A_y in range(len(A)):
        A_t[A_x].append(A[A_y][A_x])

for y in range(len(A_t)):
    print(A_t[y])

# ---- SNIP ----
