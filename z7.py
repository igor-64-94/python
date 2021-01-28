
def fact(n):
    factorial = 1
    for elem in range(1, n + 1):
        factorial = elem * factorial
        yield factorial

if __name__ == '__main__':
    n = int(input('Введите N: '))
    for el in fact(n):
        print(el)