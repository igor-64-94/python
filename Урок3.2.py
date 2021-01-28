if __name__ == '__main__':

    def printPerson(name, lastName, birthYear, city, email, phone):

        print('Имя {} фамилия {}, родился в {} году, город проживания {}. Электронная почта: {}. Номер телефона: {}.'.format(name, lastName, birthYear, city, email, phone))


    printPerson(name='Игорь', lastName='Латфулин', birthYear=1994, city='Москва', email='igor-64-94@mail.ru', phone='+7 (999)-083-78-16')