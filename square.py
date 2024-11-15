def area(a):
    '''Принимает число a, возвращает квадрат этого числа - площадь фигуры'''
    if (a >= 0):
        return a * a
    else:
        raise (ValueError)


def perimeter(a):
    '''Принимает число a, возвращает это число, умноженное на 4 - периметр фигуры'''
    if (a >= 0):
        return 4 * a
    else:
        raise (ValueError)

