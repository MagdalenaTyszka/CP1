colors = open('colors.txt', 'w')
array = ["blue","red","green"]
for i in array:
    i = i + "\n"
    colors.write(i)
colors.close()    