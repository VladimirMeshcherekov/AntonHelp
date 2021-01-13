import math
k = 1
b = -3
while b <= 4:
    try:
        cout0 = (1/(b+1.8))# + math.fabs((math.log(math.cos(b*b*b*b*b), 2))
        cout1 = math.cos(b*b*b*b*b)
        cout2 = math.log(cout1, 2)
        cout3 = math.fabs(cout2)
    except:
        print("")
    print(cout0 + cout3);    
    b=b+0.55
