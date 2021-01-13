
su = 0

# в первой строке ввода идёт количество строк массива
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)



for i in range(n):
    for j in range(n):
        if (i + j == n-1):
            su = su + a[i][j]

for row in a:
    print(' '.join([str(elem) for elem in row]))
print(su) #побочная диагональ


for j in range(n):
    for i in range(n):
        if a[i][j] < 0:
            break
        if i == n-1:
            print(j)#номер столбцов без отрицательных чисел
            
            #t.me/snappy
