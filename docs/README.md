
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
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Общее описание
- Содержит три файла rectangle.py, square.py и circle.py с функциями подсчета площади и периметра соответсвующих геометрических фигур и файл calculate.py для выполнения функций.

## Функции файлов
# rectangle.py
- area(a) принимает число а - сторону прямоугольника, возвращает квадрат этого числа - площадь фигуры.
```
a = 4
print(area(a)) //4 * 4 = 16
```
- perimeter(a) принимает число а - сторону прямоугольника, возвращает число, умноженное на 4 - периметр фигуры.
```
a = 3
print(perimeter(a)) //3 * 4 
//12
```
# circle.py
- area(r) принимает число r - радиус окружности, возвращает квадрат числа, умноженный на pi
```
r = 5
print(area(r)) // 5 * 5 * pi 
//78.53981633974483
```
- perimeter(r) принимает число r - радиус окружности, возвращает число, умноженное на 2*pi
```
r = 7
print(perimeter(r)) // 7 * 2 * pi
//43.982297150257104

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