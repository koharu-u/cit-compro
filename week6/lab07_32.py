integer = list(map(int, input("Enter integer between 1 and 100: ").split()))

integer_2 = list(set(integer))
integer_2.sort()

for i in range(len(integer_2)):
    count = integer.count(integer_2[i])
    print(f"{integer_2[i]} occurs {count} {'times' if count > 1 else 'time'}")
