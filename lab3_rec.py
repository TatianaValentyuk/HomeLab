def Squares(a, b, n):
    if (a == b):
        print("квадрат со стороной:", a, "см")
        print("Количество нарезанных фигур:", n + 1)
        return n + 1
    elif (a < b):
        print(n+1, " квадрат:")
        print("Длина ребра полученного квадрата:", a, "\n")
        return Squares(a, b - a, n + 1), n
    else:
        print(n+1, " квадрат:")
        print("Длина ребра полученного квадрата:", b,  "\n")
        return Squares(a - b, b, n + 1), n

print("Введите стороны прямоугольника (см)")
a = int(input('а=: \n'))
b = int(input('в=: \n'))
n = 0
Squares(a, b, n)