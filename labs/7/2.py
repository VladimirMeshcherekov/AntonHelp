import math
k = 1
b = -3
for b in range(-300, 400, 55):
    try:
        b=b/100
        cout0 = (1/(b+1.8))# + math.fabs((math.log(math.cos(b*b*b*b*b), 2))
        cout1 = math.cos(b*b*b*b*b)
      #  cout2 = math.log(cout1, 2)
        cout3 = math.fabs(math.log(cout1, 2))
        print(cout0 + cout3);  
    except:
        print("")
   # print(cout0 + cout3);    

#оно работает хотя не должно по логике, в теории принт должен быть в конце, но
    #оно ругается на cout3 при возникновении исключения в cout2 (шот с логарифмом)
        #а так вроде всё норм









   #t.me/snappy
