weight = eval(input("Enter weight in pounds: "))

height = (eval(input("Enter height in feet: ")) * 12)
height += eval(input("Enter height in inches: "))

weightInKilograms = weight * 0.45359237
heightInMeters = height * 0.0254
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is",bmi)
print("You are ", end="")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
