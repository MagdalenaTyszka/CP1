array = [1.2,3,4,5,8.2]
n = float(input('Podaj liczbę '))
s = str()
for i in array:
    if n > i:
        s += str(i) + " "
print(f'Liczby mniejsze od {n} to : {s}')        