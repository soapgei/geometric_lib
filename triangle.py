def area(a, b, c):
    '''Принимает три числа a, b, c - стороны треугольника, их площадь, посчитанную
    по формуле Герона'''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle")
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    '''Принимает три числа a, b, c - стороны треугольника,
    возвращает их сумму - периметр фигуры'''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle")
    return a + b + c
