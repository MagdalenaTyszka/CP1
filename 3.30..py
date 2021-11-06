x = 1
N = float(input("Enter your number: "))
for i in range (x,(N **(1/2))):
    if x % i == 0:
        print(x)
        x = x + 1
    
