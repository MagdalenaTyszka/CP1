def compar(array1,array2):
    if array1 == array2:
        print(f'Array1: {array1}')
        print(f'Array2: {array2}')
        print('Comparison: arrays are the same')
        return True
    else:
        print(f'Array1: {array1}')
        print(f'Array2: {array2}')
        print('Comparison: arrays are not the same')
        return False
        
        
compar([5,1],[5,3,1])

