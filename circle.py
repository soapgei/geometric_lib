import math


def area(r):
    '''принимает число r - радиус, возвращает квадрат этого числа, умноженный на число pi'''
    if (r >= 0):
        return math.pi * r * r
    else:
        raise (ValueError)


def perimeter(r):
    '''принимает число r - радиус, возвращает радиус умноженный на два и pi'''
    if (r >= 0):
        return 2 * math.pi * r
    else:
        raise (ValueError)
