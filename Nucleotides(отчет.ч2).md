import sys
def matrix(a, b):   # создание матрицы, первой ее строки и столбца
    mm = [[0] * (b + 1) for q in range(a + 1)]
    for i in range(1, a+1):
        mm[i][0] = mm[i - 1][0] + 1
    for j in range(1, b+1):
        mm[0][j] = mm[0][j - 1] + 1
    return mm


def mimm(i, j, mm, A, B):   # заполнение элемента массива
    if A[i-1] == B[j-1]:
        w = mm[i - 1][j - 1]
    else:
        w = mm[i - 1][j - 1] + 1
    w = min(w, mm[i-1][j] + 1, mm[i][j - 1] + 1)
    mm[i][j] = w


def printing(mm, A, B):    # вывод матрицы
    a = len(A)
    b = len(B)
    print("    ", end='')
    for j in range(0, b):
        print(B[j], end=' ')
    print()
    print("  ", end='')
    for i in range(0, a + 1):
        if i != 0:
            print(A[i - 1], end=' ')
        for j in range(0, b + 1):
            print(mm[i][j], end=' ')
        print()


def relax(mm, A, B):    # проход по элементам массива и их заполнение
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            mimm(i, j, mm, A, B)


def froppy(mm, A, B, gr, i, j):
    if i + j == 0:
        print(gr)
        print(len(gr))
    elif i != 0 and j == 0:
        gr = str(A[i-1]) + gr
        froppy(mm, A, B, gr, i - 1, j)
    elif i == 0 and j != 0:
        gr = str(B[j-1]) + gr
        froppy(mm, A, B, gr, i, j - 1)
    else:
        if A[i-1] == B[j-1]:
            gr = str(A[i-1]) + gr
            froppy(mm, A, B, gr, i - 1, j - 1)
        else:
            if mm[i - 1][j] <= mm[i][j - 1]:
                gr = str(A[i-1]) + gr
                froppy(mm, A, B, gr, i - 1, j)
            else:
                gr = str(B[j-1]) + gr
                froppy(mm, A, B, gr, i, j - 1)


def dist(A, B):    # ввод строк и вывод искомого расстояния
    a = len(A)
    b = len(B)
    sys.setrecursionlimit(a + b)
    mm = matrix(a, b)
    relax(mm, A, B)
    #printing(mm, A, B)
    gr = ""
    froppy(mm, A, B, gr, len(A), len(B))


def doing():
    A = str(input())
    B = str(input())
    print(len(A), len(B))
    dist(A, B)


doing()
