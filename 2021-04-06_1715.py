sth = input()
if '0' <= sth <= '9':print('numeric')
elif 'A' <= sth <= 'Z' or 'a' <= sth <= 'z':print('alpha')
else:print('other')