if __name__ == '__main__':

    def my_func(number1, number2, number3):

        array = [number1, number2, number3]
        array.sort()
        array.pop(0)

        return array[0] + array[1]


    print('Введите три числа.')
    num1 = int(input('Первое число: '))
    num2 = int(input('Второе число: '))
    num3 = int(input('Третье число: '))

    print('Сумма двух наибольших чисел равна {}'.format(my_func(num1, num2, num3)))
