inputStr, newStr = input(), ''
for i in range(0, len(inputStr)):
    if ord(inputStr[i]) in range(ord('a'), ord('z') + 1):
        newStr = newStr + chr((ord(inputStr[i]) - ord('a') - 3 + 1) % 26 + ord('a') - 1)
    else:
        newStr = newStr + inputStr[i]
print(newStr)