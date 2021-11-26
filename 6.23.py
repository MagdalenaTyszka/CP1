def median(array):
    l=len(array)//2
    if len(array)%2 == 1:
        median = array[l]
    else:
        median = (array[l]+ array[l - 1])/2
    print(median)

median([1,0,9,4,6])
median([6,8,3,3,1,0,5,7])        