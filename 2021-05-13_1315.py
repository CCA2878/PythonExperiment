class fbncSum:
    s = 1
    __k1 = 1
    __k2 = 1
    __k = 0

    def sum(t):
        fbncSum.s += t

    def list(n):
        if n == 2:
            fbncSum.sum(fbncSum.__k2)
        else:
            fbncSum.list(n - 1)
            fbncSum.sum(fbncSum.__k1 + fbncSum.__k2)
            fbncSum.__k = fbncSum.__k1 + fbncSum.__k2
            fbncSum.__k1 = fbncSum.__k2
            fbncSum.__k2 = fbncSum.__k

n = int(input())
fbncSum.list(n)
print(f'Fibonacci数列前{n}项和为{fbncSum.s}')