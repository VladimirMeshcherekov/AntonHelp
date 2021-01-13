string = input()
# Define your variables
result = ''
for i in string:
        if i == 'и':        #речь шла только про маленьки буквы
                i = 'ы'
        result += i
print (result)

print(string.swapcase())
print(string.center(50, ))
