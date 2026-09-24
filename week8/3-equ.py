def fx(x):
    if(x > 0):
        return((x**2)+(2*x)-1)
    else:
        return (1)

def main():
    x = eval(input("Please enter the number: "))
    print("Value of f(x) is", fx(x) )

main()
