n1, m1 = map(int, input().split())
mat1 = [[int(i) for i in input().split()] for _ in range(n1)]


def uproshenie2(n, m, mat):
    flag = True
    for i in mat:
        for delitel in range(max(i)+1, 1, -1):
            for j in range(m):
                if i[j] % delitel != 0:
                    flag = False
                    break

            if flag:
                for q in range(m):
                    i[q] //= delitel

            else:
                flag = True
    return mat


print(uproshenie2(n1, m1, mat1))
