a = int(input("Enter the length of the first side of the triangle: "))
b = int(input("Enter the length of the second side of the triangle: "))
c = int(input("Enter the length of the third side of the triangle: "))
p = (a + b + c)/ 2
S = ( p * (p - a) * (p - b) * (p - c)) ** (1/2)
print (f"The area of the triangle is {S}")