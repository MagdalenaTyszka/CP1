array= [12,6,4,9,3]
for i in array:
    g = i * "*"
    print(f'{i}:{g}')
    
def star(n):
    print(f'{n}:{n * "*"}')
    return n * "*"

star(9)