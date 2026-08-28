count_pos = 0
count_neg = 0
total = 0

while True:
    user_input = int(input("Enter an integer, the input ends if it is 0: "))
    if(user_input > 0):
        count_pos += 1
    elif(user_input < 0):
        count_neg += 1
    elif (user_input == 0):
        break
    total += user_input

if count_neg == 0 and count_pos == 0:
    print("You didn't enter any number")
else:
    print("The number of positives is", count_pos)
    print("The number of negatives is", count_neg)
    print("The total is", total)
    print("The average is", total/(count_pos+count_neg))

