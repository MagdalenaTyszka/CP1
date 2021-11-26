array=[4,3,7,1,3]
def sum(array):
    sum = 0
    for i in array:
        sum = sum + i 
    return sum

def array2str(array):
    numbers= str()
    for i in array:
        numbers = numbers + str(i) + " "
    return numbers

print(f"sum of values: {sum(array)}")        
print(f"array: {array2str(array)}")  