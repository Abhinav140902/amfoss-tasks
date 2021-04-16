a = []
b = []
N = int(input())
k = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
while (k<N):
    c.append(b[k]//a[k])
    k = k+1
print(min(c))
