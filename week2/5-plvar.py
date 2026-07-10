x = 5
a = 10
y = x + 1
print("line 1: ","x =", x, "y =", y, "a =", a, "b =", "-")
b = a // x
print("line 2: ","x =", x, "y =", y, "a =", a, "b =", b)
b += 1
print("line 3: ","x =", x, "y =", y, "a =", a, "b =", b)
x *= y - b
print("line 4: ","x =", x, "y =", y, "a =", a, "b =", b)
y += 1
print("line 5: ","x =", x, "y =", y, "a =", a, "b =", b)
a += y
print("line 6: ","x =", x, "y =", y, "a =", a, "b =", b)
