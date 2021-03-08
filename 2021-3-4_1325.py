#2021-3-4 13:28:17 tempconvert.py
tempStr = input('Temp with C or F: ')
if tempStr[-1] in ['F','f']:
    result = (eval(tempStr[0:-1]) - 32) / 1.8 #华氏度转摄氏度
    print('Result is {:.2f}C'.format(result))
elif tempStr[-1] in ['C','c']:
    result = 1.8 * eval(tempStr[0:-1]) + 32 #摄氏度转华氏度
    print('Result is {:.2f}F'.format(result))
else:
    print('嘤嘤嘤!')