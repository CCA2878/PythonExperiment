s = 0
for i in range(1, 94):#1分钱
    for j in range(1, 48):#2分钱
        for k in range(1, 20):#5分钱
            if i + (2 * j) + (5 * k) == 100:
                s += 1
print(s)