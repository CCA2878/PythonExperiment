for i in range(1, 10):
    for j in range(i, 10):
        print('{}*{}={:2}'.format(j, i, i * j), end = '  ')
    if i != 9:
        print('\n' + ('        ' * i), end="")