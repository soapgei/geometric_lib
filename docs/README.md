
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Общее описание
- Содержит два файла rectangle.py и circle.py с функциями подсчета площади и периметра соответсвующих геометрических фигур.

## Функции
# rectangle.py
- area() принимает число а - сторону квадрата, возвращает квадрат этого числа - площадь фигуры.
```
a = 4
print(area(a)) //4 * 4 = 16
```
- perimeter() принимает число а - сторону квадрата, возвращает число, умноженное на 4 - периметр фигуры.
```
a = 3
print(perimeter(a)) //3 * 4 
//12
```
# circle.py
- area() принимает число r - радиус окружности, возвращает квадрат числа, умноженный на pi
```
r = 5
print(area(r)) // 5 * 5 * pi 
//78.53981633974483
```
- perimeter() принимает число r - радиус окружности, возвращает число, умноженное на 2*pi
```
r = 7
print(perimeter(r)) // 7 * 2 * pi
//43.982297150257104
```

## История
commit 86edb1c3dd57fa9abc7ba2ec7052507938084727 (origin/release)
Author: Danny <bublikplushka@yandex.ru>
Date:   Mon Apr 19 15:15:14 2021 +0300

    L-05: Update Docs. Add user agreement info

commit 438b89a1dfc58d90e9036fe431771427965cd1ff
Author: Danny <bublikplushka@yandex.ru>
Date:   Mon Apr 19 15:12:19 2021 +0300

    L-05: Add user agreement

commit 6adb96248a4d00d3bea13bd95d78ef52352cd1b4
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 30494317cde4419be779c14306561e0eaa78b88b (origin/feature)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:36:09 2021 +0300

    L-04: Add rectangle.py
