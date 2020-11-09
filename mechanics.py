def comby(A, B, ia, ib, k, j, Q):    # смешивание строк
    if len(A) - ia == 0:  # если мы дошли до конца 1 строки
        for q in range(ib, len(B)):
            Q[j] = Q[j] + B[q]
    elif len(B) - ib == 0:      # если мы дошли до конца 2 строки
        for q in range(ia, len(A)):
            Q[j] = Q[j] + A[q]
    elif A[ia] == B[ib]:        # если элементы двух строк совпадают
        Q[j] = Q[j] + A[ia]
        comby(A, B, ia + 1, ib + 1, k, j, Q)
    else:                       # если элементы двух строк различные
        if k == 1:
            Q[j] = Q[j] + A[ia]
            comby(A, B, ia + 1, ib, k, j, Q)
        elif k == 0:
            Q[j] = Q[j] + B[ib]
            comby(A, B, ia, ib + 1, k, j, Q)


A = str(input())
B = str(input())
if len(A) > len(B):
    (A, B) = (B, A)        # не уверен, что это принципиально, но иначе прога не работает))
a = len(A)
b = len(B)
Q = []                      # создадим массив, состоящий из строк. В него мы будем вставлять наших франкенштейнов
for i in range(a):
    Q.append("")
l = a + b
s = 0
for i in range(a):
    for j in range(i):
        Q[i] = Q[i] + A[j]
    comby(B, A, 0, i, 1, i, Q)
    if len(Q[i]) < l:
        s = i
        l = len(Q[i])
print("количество символов первой последовательности:", a)
print("количество символов второй последовательности:", b)
print(Q[s])
print("количество символов в полученной последовательности:", l)
