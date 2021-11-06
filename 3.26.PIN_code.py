PIN = "0805"
possibilities = 3
while possibilities > 0:
    x = input("Enter the PIN code: ")
    if x == PIN:
        print ("Correct!")
        possibilities = 0
    else:
        possibilities = possibilities - 1
        print ("Incorrect...")
if x != PIN and possibilities == 0:
    print ("Sorry, your payment card has been blocked.")
           