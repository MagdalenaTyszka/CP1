array = [8,2,5,1,9]
array1 = str()
power = str()
for i in array:
    array1 = array1 + str(i) + " " 
    power = power + str(i**2) + " "
print(f'existed array: {array1}')
print(f'2nd power: {power}')