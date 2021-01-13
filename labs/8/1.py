import math
l = []
z = []
sr = []
i = 0
t = input()
t = int(t)
while i<12:
    d = input()
    d= int(d);
    l.append(d)
    z.append(t*t*t + math.log(d)* math.log(d)) #если оно тут крашнется то виноват юзер
    if (t*t*t + math.log(d)* math.log(d)) > 0:
        sr.append((t*t*t + math.log(d)* math.log(d))) #если оно тут не будет работать то скопируй значение с 9й строки
    i=i+1
    
#print(l)
sred = 0;
x = len(sr)
while x > 0:
    sred = sr[x-1] + sred
    x=x-1
sred = sred / len(sr)

print(z)
z[2] = sred
print(z)


#на редкость я даже отдебажил, ничего падать не должно
    #t.me/snappy
