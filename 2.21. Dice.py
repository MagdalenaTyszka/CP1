import random
dice = (1, 2, 3, 4, 5, 6)
first_roll = random.choice(dice)
second_roll = random.choice(dice)
third_roll = random.choice(dice)
sum = first_roll + second_roll + third_roll
print(f"Your results are {first_roll},{second_roll},{third_roll} and sum is {sum}")