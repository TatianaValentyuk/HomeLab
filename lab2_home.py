# import random
# #Вариант 4
# #Найдите произведение элементов списка с нечетными номерами.
#
#
# n = int(input("Введите длину списка: \n"))
# A = []
#
# for i in range(n):
#     A.append(random.randint(-10, 10))
# print("Список ")
# print(A)
# mult=A[0]
# for i in range(1, len(A)):
#     if ((i%2)==0):
#         mult = mult*A[i]
#
# print(f"Произведение элементов списка с нечетными номерами равно {mult}")
#
# #Найдите наибольший элемент списка, затем удалите его и выведите новый список.
# max=max(A)
# print(f"Наибольший элемент списка равен {max}")
# count=0
# for y in range(len(A)):
#     if (A[y]==max):
#         count=count+1
# print(f"В списке {count} максимальный(х) эл-т(ов)")
# for el in range (count):
#     A.remove(max)
#
# print(f"Измененный список {A}")
# 2.	Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

import random

n = int(input("Введите размер матрицы \n"))
print (f"Введите квадратную матрицу размером {n}")
V = []
for i in range(n):
        V.append([int(j) for j in input().split()])
flag = 1
for i in range(len(V)):
    if (flag==0):
        break
    for j in range(1,len(V)):
        if (V[i][j]!=V[j][i]):
            flag=0
            break
if (flag):
    print("Матрица симетричная")
else:
    print(f"Матрица не симетричная")

# A = [[1,3,0], [3,2,6], [0,6,5]]
# print(A)
# flag=1
# for i in range(len(A)):
#     if (flag==0):
#         break
#     for j in range(1,len(A)):
#         if (A[i][j]!=A[j][i]):
#             flag=0
#     break
# if (flag):
#     print("Матрица симетричная")
# else:
#     print(f"Матрица не симетричная")


