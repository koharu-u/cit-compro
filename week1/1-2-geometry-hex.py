import math
vertex_len = eval(input("Enter the length from the center to a vertex: "))
print("The area of pentagon is", (3*math.sqrt(3))/(2)*(((2*vertex_len)*math.sin(math.pi/5))**2))
