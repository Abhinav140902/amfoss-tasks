def trib(i):
    if i in {1,2,3}:
        return i
    else:
        a = 1
        b = 2
        c = 3
        for j in range(3,i):
            p = a+b+c
            a = b
            b = c
            c = p
        return(p) 
T = int(input())
while(T):
    i = int(input())
    k = int(trib(i)%(10**9 +7))
    p = str(k).rstrip('0')
    print(int(p[::-1]))         
    T-=1
