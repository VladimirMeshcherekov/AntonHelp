print(ord("9"))
string = input()
cout =  -1
new_string = ""
for i in  string:
    print(cout, " ", new_string)
    if ord(i) > 57:

        #new_string += i
        if (cout%2 == 0) & (cout != 4):
            if i.isupper():
                new_string += i.lower()
            else:
                new_string += i.upper()
        else:
            new_string += i

    else:
        new_string += i
    cout = cout + 1
print(new_string)

#в душе не ебу почему она работает, но важен результат, и да, на момент комита 2:45
