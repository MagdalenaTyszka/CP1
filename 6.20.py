def occurs(number, array):
    if number in array:
        print(f'Number: {number}')
        print(f'Array: {array}')
        print(f'Result: number {number} appears in array')
        return True
    else:
        print(f'Number: {number}')
        print(f'Array: {array}')
        print(f'Result: number {number} not appears in array')

occurs(15,[15, 38, 7, 23, 14])