inputStr = input()
newStr = []
for i in range(len(inputStr)):
    if not ord('A') <= ord(inputStr[i]) <= ord('Z'):
        newStr.append(inputStr[i])
print(''.join(newStr))