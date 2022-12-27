weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height * height)

category = " "
if bmi >= 30:
 category = "obese"
elif bmi >= 25:
 category = "overweight"
elif bmi >= 18.5:
 category = "normal"
elif bmi < 18.5:
 category = "underweight"
else:
 print("invalid")

print(f"User's BMI is: {bmi} and they are {category}")

