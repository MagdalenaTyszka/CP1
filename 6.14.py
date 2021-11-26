array=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longname=array[0]
for i in array:
    if len(i) > len(longname):
        longname = i

print('Names: Genowefa Onufry Celestyna Alojzy Pankracy')
print(f'Longest name: {longname}')