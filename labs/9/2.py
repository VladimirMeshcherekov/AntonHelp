n = 2
su = 0
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input()) #ввод ебанутый, но решение лучше я пока не придумал
        if (i + j == n-1):
            su = su + a[i][j]

for row in a:
    print(' '.join([str(elem) for elem in row]))
print(su) #побочная диагональ

print(a[0][1])

for j in range(n):
    for i in range(n):
        if a[i][j] < 0:
            break
        if i == n-1:
            print(j)#номер столбцов без отрицательных чисел
            
            #t.me/snappy
