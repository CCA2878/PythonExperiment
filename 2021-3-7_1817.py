n = eval(input())
i = 0
N = []
text = ''
while i <= 5:
    N.append(str(n**i))#用append在列表末尾添加元素
    i += 1
text = ' '.join(N)
print(text)