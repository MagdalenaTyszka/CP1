height = input("Enter your height in cm: ")
weight = input("Enter your weight in kg: ")
height = float(height)/100
weight = float(weight)
print(f"BMI index: {weight // ((height) ** 2)}")
