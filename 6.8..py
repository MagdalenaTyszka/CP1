
array=[(-15), 8,(-31), 47,(-2), 19]
min=array[0]
max=array[0]
for i in array:
    if i < min:
        min = i
    elif i > max:
        max = i
print(f'min= {min} ,max= {max}')