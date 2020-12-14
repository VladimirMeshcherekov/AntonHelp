import math
str = input("дай строку")
a = len(str)
i = 0
timer = 1
cout = ""

while i< len(str):
    if str[i] == ' ':
        timer = 1;
        #print(" ", "t=", timer) пусть будет для откладки
        cout = cout + str[i];

    else:
        if ((timer % 2 == 0) & (timer != 0)):
            #print(str[i], str[i]) пусть будет для отладки
            timer = timer + 1
            cout = cout + str[i];
            cout = cout + str[i];

        else:
            timer = 1 + timer
            #print(str[i]) пусть будет для отладки
            cout = cout + str[i];

    i= i + 1;
    
print(cout)
