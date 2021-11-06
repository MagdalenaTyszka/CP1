import random
dice = [1, 2, 3, 4, 5, 6]
i = random.choice(dice)
user_number = input("Enter your number from 1 to 6: ")
user_number = int(user_number)
if i == user_number:
    print("True")
else:
    print(f"You don't guess! The dice number is {i}")