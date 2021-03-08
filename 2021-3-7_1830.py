m = eval(input())
n = eval(input())
N = []
text = ''
N.append(str(m + n))
N.append(str(m * n))
N.append(str(m ** n))#^为异或运算符
N.append(str(m % n))
N.append(str(max(m,n)))
text = ' '.join(N)
print(text)