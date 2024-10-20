
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
<<<<<<< HEAD
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Общее описание
- Содержит три файла rectangle.py, square.py и circle.py с функциями подсчета площади и периметра соответсвующих геометрических фигур и файл calculate.py для выполнения функций.

## Функции файлов
# rectangle.py
- area(a) принимает число а - сторону прямоугольника, возвращает квадрат этого числа - площадь фигуры.
=======
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Общее описание
- Содержит два файла rectangle.py и circle.py с функциями подсчета площади и периметра соответсвующих геометрических фигур.

## Функции
# rectangle.py
- area() принимает число а - сторону квадрата, возвращает квадрат этого числа - площадь фигуры.
>>>>>>> 2a64af26aee01e6f4ceff4f0e0cfb49f5775d80d
```
a = 4
print(area(a)) //4 * 4 = 16
```
<<<<<<< HEAD
- perimeter(a) принимает число а - сторону прямоугольника, возвращает число, умноженное на 4 - периметр фигуры.
=======
- perimeter() принимает число а - сторону квадрата, возвращает число, умноженное на 4 - периметр фигуры.
>>>>>>> 2a64af26aee01e6f4ceff4f0e0cfb49f5775d80d
```
a = 3
print(perimeter(a)) //3 * 4 
//12
```
# circle.py
<<<<<<< HEAD
- area(r) принимает число r - радиус окружности, возвращает квадрат числа, умноженный на pi
=======
- area() принимает число r - радиус окружности, возвращает квадрат числа, умноженный на pi
>>>>>>> 2a64af26aee01e6f4ceff4f0e0cfb49f5775d80d
```
r = 5
print(area(r)) // 5 * 5 * pi 
//78.53981633974483
```
<<<<<<< HEAD
- perimeter(r) принимает число r - радиус окружности, возвращает число, умноженное на 2*pi
=======
- perimeter() принимает число r - радиус окружности, возвращает число, умноженное на 2*pi
>>>>>>> 2a64af26aee01e6f4ceff4f0e0cfb49f5775d80d
```
r = 7
print(perimeter(r)) // 7 * 2 * pi
//43.982297150257104
<<<<<<< HEAD

# square.py
- area(a) принимает число а - сторону квадрата, возвращает квадрат этого числа - площадь фигуры.
```
a = 4
print(area(a)) //4 * 4 = 16
```
- perimeter(a) принимает число а - сторону квадрата, возвращает число, умноженное на 4 - периметр фигуры.
```
a = 3
print(perimeter(a)) //3 * 4 
//12
```

# triangle.py
- area(a,b,c) принимает числa а, b, c - стороны треугольника, возвращает сумму чисел, деленную на 2 - площадь фигуры.
```
a = 4
b = 3
c = 5
print(area(a,b,c)) //(a+b+c)/2 = 6 
```
- perimeter(a) принимает числa а, b, c - стороны треугольника, возвращает сумму чисел - периметр фигуры.
```
a = 4
b = 3
c = 5
print(perimeter(a,b,c)) //(a+b+c) = 12
```
## История
commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300
=======
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
>>>>>>> 2a64af26aee01e6f4ceff4f0e0cfb49f5775d80d
