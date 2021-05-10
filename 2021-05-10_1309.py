def fact(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s

num = input().split(',')
print('{:.2f}'.format(fact(int(num[0])) / (fact(int(num[1])) * fact(int(num[0]) - int(num[1])))))