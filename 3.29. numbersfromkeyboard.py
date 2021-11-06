quantity = 0
suma = 0
mean = 0
y = 0
x = 1
while x != 0 :
    x = input("Enter number: ")
    x = int(x)
    if x == 0:
        print (f"RESULT: Quantity={quantity}, Sum={suma}, Mean={mean}")
    else:
        y = x + y
        quantity = quantity + 1
        suma = suma + x
        mean = suma / quantity
        