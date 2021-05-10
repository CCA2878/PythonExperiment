def triAngle(inputStr):
    try:
        num = (inputStr).split(',')
        if float(num[0]) + float(num[1]) <= float(num[2]) or float(num[0]) + float(num[2]) <= float(num[1]) or float(num[1]) + float(num[2]) <= float(num[0]) or float(num[0]) <= 0 or float(num[1]) <= 0 or float(num[2]) <= 0:
            return 0.00
        else:
            return ((4 * float(num[1]) ** 2 * float(num[2]) ** 2 - (float(num[0]) ** 2 - float(num[1]) ** 2 -float(num[2]) ** 2) ** 2) ** 0.5) * 0.25
    except:
        return 0.00

print('{:.2f}'.format(triAngle(input())))
