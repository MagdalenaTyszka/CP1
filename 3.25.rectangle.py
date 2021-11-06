a = input(" Enter dimension a: ")
a = int(a)
b = input(" Enter dimension b: ")
b = int(b)
c = b - 4
print ("*" * b)
for x in range (1,a - 1):
    print ("*"," " * c, "*")
print ("*" * b)    