num = (input()).split(',')
if float(num[0]) + float(num[1]) <= float(num[2]) or float(num[0]) + float(num[2]) <= float(num[1]) or float(num[1]) + float(num[2]) <= float(num[0]):
    print(f'边长{num[0]},{num[1]},{num[2]}不能构成三角形。')
elif float(num[0]) == float(num[1]) and float(num[0]) == float(num[2]):
    S = ((4 * float(num[1]) ** 2 * float(num[2]) ** 2 - (float(num[0]) ** 2 - float(num[1]) ** 2 -float(num[2]) ** 2) ** 2) ** 0.5) * 0.25
    print('边长{},{},{}能构成等边三角形，它的面积是{:.1f}。'.format(num[0], num[1], num[2], S))
elif float(num[0]) ** 2 + float(num[1]) ** 2 == float(num[2]) ** 2 or float(num[0]) ** 2 + float(num[2]) ** 2 == float(num[1]) ** 2 or float(num[1]) ** 2 + float(num[2]) ** 2 == float(num[0]) ** 2:
    S = ((4 * float(num[1]) ** 2 * float(num[2]) ** 2 - (float(num[0]) ** 2 - float(num[1]) ** 2 -float(num[2]) ** 2) ** 2) ** 0.5) * 0.25
    print('边长{},{},{}能构成直角三角形，它的面积是{:.1f}。'.format(num[0], num[1], num[2], S))
else:
    S = ((4 * float(num[1]) ** 2 * float(num[2]) ** 2 - (float(num[0]) ** 2 - float(num[1]) ** 2 -float(num[2]) ** 2) ** 2) ** 0.5) * 0.25
    print('边长{},{},{}不能构成直角三角形，也不能构成等边三角形，它的面积是{:.1f}。'.format(num[0], num[1], num[2], S))