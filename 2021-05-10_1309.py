def runnian(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
y=int(input())
if runnian(y) == True:
    print("%d年是闰年"%y)
else:
    print("%d年不是闰年"%y)