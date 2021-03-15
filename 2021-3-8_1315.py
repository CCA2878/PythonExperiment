#九九乘法表
for j in range(9,0,-1):
    resultStrlist = []
    for i in range(1,j + 1):
        resultStrlist.append('{}*{}={}'.format(j , i , i * j))
    print(' '.join(resultStrlist))