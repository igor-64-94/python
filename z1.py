import sys

def calculate_salary(pph, noh, bonus):
    return pph * noh + bonus

if __name__ == '__main__':
    if len(sys.argv) == 4:
        pph, noh, bonus = map(float, sys.argv[1:])
        salary = calculate_salary(pph, noh, bonus)
        print('%.2f' % salary)
    else:
        raise Exception('Not enough arguments!')