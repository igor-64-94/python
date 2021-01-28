if __name__ == '__main__':

    def int_func(myword):

        return myword.title()


    myText = input('Введите текст из строчных латинских букв: ')

    newText = (' '.join([int_func(item) for item in myText.split(' ')]))
    print(newText)
