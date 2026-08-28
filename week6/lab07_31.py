scores = list(map(int, input("Enter Scores: ").split()))
grades= ["F","A","B","C","D"]
max_score = max(scores)
for loop in range(0,len(scores)):
    print(f"Student {loop} is {scores[loop]} and grade is ", end="")
    for i in range(1,5):
        if(scores[loop] >= max_score - (i * 10)):
            print(grades[i])
            break
    if(scores[loop] < max_score-40):
            print(grades[0])
