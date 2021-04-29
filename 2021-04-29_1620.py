level = int(input())
n = [[1], [1, 1]]
for i in range(2, level):#生成数列列表
    n.append([1])
    for j in range(i - 1):
        n[i].append(n[i - 1][j] + n[i - 1][j + 1])
    n[i].append(1)

for str1 in n:#按傻逼到不能再傻逼的格式输出
    print(' ' * ((level - n.index(str1) - 1) * 3 - 1), end = '')
    if n.index(str1) != level - 1:
        if n.index(str1) == 0:
            for str2 in str1:
                print('{:3}'.format(str2), end = '')
            print(' ')
        else:
            for str2 in str1:
                print('{:3}'.format(str2), end = '   ')
            print(' ')
    else:
        for str2 in str1:
            print('{:2}'.format(str2), end = '    ')
        print('')