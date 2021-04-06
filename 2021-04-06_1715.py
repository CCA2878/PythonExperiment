num = (input()).split(',')
if float(num[0]) <= 0 or float(num[1]) <= 0 or num[0].count('.') != 0 or num[1].count('.') != 0:
    print('输入数据错误！')
elif float(num[0]) % float(num[1]) == 0.0:
    print(f'{num[1]}是{num[0]}的因数。')
else:
    print(f'{num[1]}不是{num[0]}的因数。')