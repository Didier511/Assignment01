#BMI Calculator
#13th August 
# Assignment

print("\nWelcome to your Body Mass Index calculator!\nPlease enter your details")
print("*"*50)
#accept user data
height=float(input("\nEnter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))

#Calculate BMI
bmi=weight/(height**2)
print("\n-Your BMI is:",round(bmi,2))

#Category
if bmi<18.6:
    category="Underweight."
elif bmi<26:
    category="Normal weight."
elif bmi<31:
    category="Overweight."
else:
    category="Obese"
print(f"-Category: {category}\n")

#separation line
print("*"*50)

