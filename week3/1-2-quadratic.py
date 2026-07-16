from math import sqrt

a, b , c = eval(input("Enter a, b, c: "))

quadeq = (b**2)-(4*a*c)
if (quadeq < 0):
    print("The equation has no real roots")
elif (quadeq == 0):
    print("The root is", (-b-sqrt(quadeq))/(2*a))
elif (quadeq > 0):
    print("The roots are", (-b+sqrt(quadeq))/(2*a), "and", (-b-sqrt(quadeq))/(2*a))

