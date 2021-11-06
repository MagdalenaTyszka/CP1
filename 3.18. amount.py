coin_1 = 1
coin_2 = 2
coin_3 = 5
amount = input("Enter the amount in PLN: ")
x = int(amount) // coin_3
y = (int(amount) - coin_3 * x ) // coin_2
z = (int(amount) - coin_3 * x - coin_2 * y ) // coin_1
print ("The amount of PLN", amount, "in coins:\n5 zł -", x, "\n2 zł -", y, "\n1 zł -",z)  