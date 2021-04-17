t = int(input())
while(t):
    N = list(map(int, input().split()))
    K = list(map(int, input().split()))
    m = max(K)
    pb=K.index(m)
    K[pb] = m-N[1]
    s = 1
    for i in K:
        s = s*i
    print(s)
    t = t-1
