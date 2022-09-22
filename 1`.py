n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]


def umnojenie(stroki1, stolb1, mat1, stroki2, stolb2, mat2):
    matrixC = [[0] * stolb2 for _ in range(stroki1)]

    for i in range(stroki1):
        for j in range(stolb2):
            for q in range(stolb2):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

    return matrixC

print(umnojenie(n, matrixA, k, matrixB))