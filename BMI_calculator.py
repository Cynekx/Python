# BMI calculator

weight = float(input("What is your weight in kg? "))



height = float(input("What is your height in meters? "))


BMI = weight/(height ** 2)


print("Your BMI is {:.2f}".format(BMI))
''' https://www.flynerd.pl/2017/01/python-3-formatowanie-napisow.html '''

if BMI <= 18:
    print("You are underweight")
if BMI >18 and BMI <= 24.9:
    print("You are in perfect shape!")
else:
    print("You are overweight")
