from upro import *

poryadok = int(input('Введите количество строк матрицы: '))
A = [[int(i) for i in input('Введите стороку множетелей: ').split()] for _ in range(poryadok)]
print()
B = [[int(i) for i in input('Введите значение выражения: ').split()] for _ in range(poryadok)]
print()

A_obrat = obratnaya(A, poryadok)
X = umnojenie(len(A_obrat), len(A_obrat[0]), A_obrat, len(B), len(B[0]), B)
count = 1
for i in range(poryadok):
    for j in range(len(X[i])):
        print('неизвестная x', count, ' = ', X[i][j], sep='')
        count += 1

print(A_obrat)