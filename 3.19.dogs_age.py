dogs_age = input("Enter the dog's age in human years: ")
dogs_age = float(dogs_age)
x = 10.5
y = 4 
if (dogs_age - 2 > 0):
    human_age1 = x * 2
    human_age2 = human_age1 + (dogs_age - 2) * y
    print ( "The dog's age in dog’s years is", human_age2, "years.")
else:
    human_age1 = x * dogs_age
    print ( "The dog's age in dog’s years is", human_age1, "years.")