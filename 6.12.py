array = [15, 8, 31, 47, 2, 19]
reverse = str()
array1 = str()
for i in array:
    reverse = str(i) + " " + reverse
    array1 = array1 + str(i) + " "
print(f'existed array: {array1}')
print(f'existed array: {reverse}')