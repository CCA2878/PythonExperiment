num = (input()).split(',')
if float(num[0]) == 0 and float(num[1]) == 0:
    print(f'点（{num[0]}，{num[1]}）是坐标原点。')
elif float(num[0]) == 0 and float(num[1]) != 0:
    print(f'点（{num[0]}，{num[1]}）在y轴上。')
elif float(num[0]) != 0 and float(num[1]) == 0:
    print(f'点（{num[0]}，{num[1]}）在x轴上。')
elif float(num[0]) > 0 and float(num[1]) > 0:
    print(f'点（{num[0]}，{num[1]}）属于第一象限。')
elif float(num[0]) < 0 and float(num[1]) > 0:
    print(f'点（{num[0]}，{num[1]}）属于第二象限。')
elif float(num[0]) < 0 and float(num[1]) < 0:
    print(f'点（{num[0]}，{num[1]}）属于第三象限。')
elif float(num[0]) > 0 and float(num[1]) < 0:
    print(f'点（{num[0]}，{num[1]}）属于第四象限。')