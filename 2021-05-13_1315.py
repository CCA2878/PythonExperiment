class HNT:#汉诺塔递归
    m = 0
    
    def prt(k, N, M):#print，顺便作为递归终点
        HNT.m += 1
        print(f'{k}:{N}-->{M}')

    def move(n, A, B, C):
        if n == 1:
            HNT.prt('1', A, C)
        else:
            HNT.move(n - 1, A, C, B)
            HNT.prt(n, A, C)
            HNT.move(n - 1, B, A, C)

HNT.move(int(input()), 'A', 'B', 'C')
print(f'总共移动了{HNT.m}次。')