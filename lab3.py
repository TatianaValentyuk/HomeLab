import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


def InsertSort(A):  # сортировка вставками
    for i in range(len(A)):
        t = A[i]
        j = i
        while (j - 1 >= 0) and (A[j - 1] > t):
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
        A[j] = t


def SelectSort(A):  # сортировка выбором
    for i in range(len(A) - 1):
        m = i
        j = i + 1
        while j < len(A):
            if A[j] < A[m]:
                m = j
            j += 1
        A[i], A[m] = A[m], A[i]
        i += 1

def SelectShaker(A):  # сортировка шейкерная
    for i in range(len(A)//2):
        for j in range(i, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i+1, -1):
            if A[j] < A[j - 1]:
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a




table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время вставкой", "Время выбором", "Время шейкерная"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        # A.append(int(round(random.random() * (max - min) + min)))
        A.append(random.randint(1,N));

    print("\nИсходный список А:")
    print(A)

    B = A.copy()
    C = A.copy()
    D = A.copy()
    E = A.copy()
    # print(B)

    # BubbleSort(A)
    #print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    # print("---")
    # print(B)

    # InsertSort(C)
    # print("---")
    # print(C)

    #SelectShaker(E)
    # print("---")
    # print(E)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")
    print("Результат пузырьковой сортировки")
    print(A)

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")
    print("Результат быстрой сортировки")
    print(B)

    t5 = datetime.datetime.now()
    InsertSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Сортировка вставкой   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")
    print("Результат сортировки вставкой")
    print(C)

    t7 = datetime.datetime.now()
    SelectSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Сортировка выбором   " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")
    print("Результат сортировки выбором")
    print(D)

    t9 = datetime.datetime.now()
    SelectShaker(E)
    t10 = datetime.datetime.now()
    y5.append((t10 - t9).total_seconds())
    print("Сортировка шейкерная   " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")
    print("Результат шейкерной сортировки")
    print(D)

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()),
         str((t8 - t7).total_seconds()),  str((t10 - t9).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")
plt.plot(x, y5, "#000000")#черный - шейкерная
plt.show()