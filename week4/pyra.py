py_lines = int(input("enter the number of lines: "))
col = 1
while(col <= py_lines):
    row = py_lines
    while(row > 0):
        if(row > col):
            print(" ", end="    ")
        elif(row <= col):
            print(row, end="    ")
        row -= 1
    row = 2
    while row <= col:
        print(row, end="    ")
        row += 1
    print()
    col += 1

