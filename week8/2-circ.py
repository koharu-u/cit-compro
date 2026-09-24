def main():
    radius = inputValue()
    area = calArea(radius)
    showArea(area)

def inputValue():
    return(int(input("Enter the radius: ")))

def calArea(radius):
    return(round(3.14159 * (radius**2), 4))

def showArea(area):
    return(print(area))

main()
