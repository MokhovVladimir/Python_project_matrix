def socrashenie(n1, n2):
    for i in range(min(abs(n1), abs(n2)), 2, -1):
        if n1 % i == 0 and n2 % i == 0:
            while n1 % i == 0 and n2 % i == 0:
                n1 /= i
                n2 /= i
    if n1 < 0 and n2 < 0:
        return str(abs(int(n1))) + '/' + str(abs(int(n2)))
    elif n1 * n2 < 0:
        return '-' + str(abs(int(n1))) + '/' + str(abs(int(n2)))
    else:
        return str(int(n1)) + '/' + str(int(n2))


def opredelitel_1_poryadka(mat_1_poryadka):
    return mat_1_poryadka[0][0]


def opredelitel_2_poryadka(mat_2_poryadka):
    return mat_2_poryadka[0][0] * mat_2_poryadka[1][1] - mat_2_poryadka[0][1] * mat_2_poryadka[1][0]


def opredelitel_3_poryadka(mat_3_poryadka):
    ''' Определитель считаестся через вычеркивание
    тк есть функция для определения второго порядка'''

    opredelitel_3 = 0
    i = 0

    for j in range(3):
        mat_new = mat_3_poryadka.copy()
        del mat_new[i]

        for num in range(len(mat_new)):
            mat_new[num] = mat_new[num][:j] + mat_new[num][j + 1:]

        opredelitel_3 += (-1)**(i + j + 2) * mat_3_poryadka[i][j] * opredelitel_2_poryadka(mat_new)

    return opredelitel_3


def opredelitel_4_poryadka(mat_4_poryadka):
    opredelitel_4 = 0
    i = 0

    for j in range(4):
        mat_new = mat_4_poryadka.copy()
        del mat_new[i]

        for num in range(len(mat_new)):
            mat_new[num] = mat_new[num][:j] + mat_new[num][j + 1:]

        opredelitel_4 += (-1) ** (i + j + 2) * mat_4_poryadka[i][j] * opredelitel_3_poryadka(mat_new)

    return opredelitel_4


def prisoed_mat(lybaya_mat, poryadok):  # Сначала передаем матрицу, потом ее порядок

    listwow = {1: opredelitel_1_poryadka, 2: opredelitel_2_poryadka, 3: opredelitel_3_poryadka, 4: opredelitel_4_poryadka}

    d = [[]]
    itog = [[]]

    for i in range(poryadok):
        for j in range(poryadok):
            element_new = 0
            mat_new = lybaya_mat.copy()
            del mat_new[i]

            for num in range(len(mat_new)):
                mat_new[num] = mat_new[num][:j] + mat_new[num][j + 1:]

            element_new += (-1) ** (i + j + 2) * listwow[poryadok - 1](mat_new)

            d[-1].append(element_new)
        d.append([])

    for i in range(len(d[:len(d) - 1])):

        for j in range(len(d[:len(d) - 1][i])):
            itog[-1].append(d[j][i])

        itog.append([])

    return itog[:len(itog) - 1]


def umnojenie(stroki1, stolb1, mat1, stroki2, stolb2, mat2):
    matrixC = [[0] * stolb2 for _ in range(stroki1)]

    for i in range(stroki1):
        for j in range(stolb2):
            for q in range(stolb2):
                matrixC[i][j] += mat1[i][q] * mat2[q][j]

    return matrixC


def obratnaya(mat, N):
    obratka = []
    listwow = {1: opredelitel_1_poryadka, 2: opredelitel_2_poryadka, 3: opredelitel_3_poryadka, 4: opredelitel_4_poryadka}
    if listwow[N](mat) != 0:

        for i in prisoed_mat(mat, N):
            for j in i:
                if j % listwow[N](mat) == 0:
                    obratka.append([j // listwow[N](mat)])
                else:
                    obratka.append([j / listwow[N](mat)])
        return obratka

    else:
        print('Матрица не имеет обратной')
        return None


def uproshenie2(n, m, mat):
    flag = True
    for i in mat:
        for delitel in range(2, max(i)+1):
            for j in range(m):
                if not flag:
                    break
                if i[j] % delitel != 0:
                    flag = False

            if flag:
                for q in range(m):
                    i[q] //= delitel

            else:
                flag = True
    return mat


def stair_type_mat(n, m, mat):
    for colvo in range(m - 1):
        general = 1
        for i in range(-(n - colvo), 0):
            general *= mat[i][colvo]

        if general != 0:
            for i in range(colvo, n):
                mnoj = general // mat[i][colvo]
                for j in range(m):
                    mat[i][j] = mat[i][j] * mnoj

            for i in range(1 + colvo, n):
                for j in range(m):
                    mat[i][j] = mat[i][j] - mat[colvo][j]

        else:
            continue
    return mat
