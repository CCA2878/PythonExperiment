inputStr = input()
newStr = []
s = 0
for i in range(len(inputStr)):
    if ord('A') <= ord(inputStr[i]) <= ord('Z'):
        newStr.append(chr(ord(inputStr[i]) + 32))
        s += 1
    elif ord('a') <= ord(inputStr[i]) <= ord('z'):
        newStr.append(chr(ord(inputStr[i]) - 32))
        s += 1
    else:
        newStr.append(inputStr[i])
print(f'共输入{s}个字母,替换后为"' + ''.join(newStr) + '".')