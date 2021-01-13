def printout():
    print("-----------------------")
    print(i)
    print(j)
    print("-----------------------")
    return 0

def printout1():
    print("-----------------------")
    print(i)
    print(j)
    print(ij1)
    print("-----------------------")
    return 0



tx1 = "1 2 3 4 5"
tx2 = "1 2 3 4 5"
i = tx1.split(" ")
j = tx2.split(" ")

i.append(55)
printout()

k = j.pop(1) #допустим это второй элемент
printout()

j[2] = 33;
printout()

ij1= []
ij1.extend(i)
ij1.extend(j)
printout1()


b = 0
while b < len(ij1):
    ij1[b] = int(ij1[b])
    b=b + 1 
    
ij1.sort()
ij1.reverse()
printout1()


