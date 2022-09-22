n1, m1 = map(int, input().split())
mat1 = [[int(i) for i in input().split()] for _ in range(n1)]


def is_stair_type(n, m, mat):
    colvo = 0
    for _ in range(n-1):
        colvo1 = 0
        for i in range(1, n):
            for j in range(m):
                if mat[i][j] != 0:
                    break
                else:
                    colvo1 += 1
        print(colvo1)
        if colvo >= colvo1:
            return False
        else:
            colvo = colvo1  
    return True


print(is_stair_type(n1, m1, mat1))
