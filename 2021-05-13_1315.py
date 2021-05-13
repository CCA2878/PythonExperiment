class factSum:
    s = 0

    def sum(t):
        factSum.s += t

    def fact(n):
        __t = 1
        for __i in range(1, n + 1):
            __t = __t * __i
        return __t

    def calc(n):
        if n == 1:
            factSum.sum(1)
        else:
            factSum.calc(n - 1)
            factSum.sum(factSum.fact(n))

factSum.calc(int(input()))
print(factSum.s)