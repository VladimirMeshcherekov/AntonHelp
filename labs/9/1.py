import math
sr = 0
per = 0
sto = 1
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n): #сперва столбец, потом строка
    for j in range(n):
            a[i][j] = math.sqrt(2*i) + math.tan(j)
            sr = a[i][j];
            if j == 0:
                per = per + a[i][j]
            if i == 1:
                sto = sto * a[i][j]

#for row in a:                                      #вывод матрицы на случай дебага
 #   print(' '.join([str(elem) for elem in row]))

sr = sr / (n*n)
print(sr) #средняя арифмитическая матрицы
print(per) #сумма первого стобца
print(sto) #произведение второй строки
