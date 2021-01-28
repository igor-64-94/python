if __name__ == '__main__':

    def division(number1, number2):

        return number1 / number2


    num1 = int(input('Введите делимое: '))
    num2 = int(input('Введите делитель: '))
    if num2 == 0:
        while num2 == 0:
            num2 = int(input('На ноль делить нельзя! Повторите ввод: '))

    print('{} / {} = {:.2f}'.format(num1, num2, division(num1, num2)))
