import math
vertex_len = eval(input("Enter the length from the center to a vertex: "))
print("The area of pentagon is", (((5/4)*(((2*vertex_len)*math.sin(math.pi/5))**2))*((math.cos(math.pi/5))/(math.sin(math.pi/5)))))

