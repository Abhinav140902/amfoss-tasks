t = int(input())
for x in range(0, t):
    k = int(input())
    sentence = list(map(str, input().split()))
    a = 0
    if k <= (len(sentence)-1):
        for y in sentence[k]:
            a = a + ord(y)
        print(a)
    else:
        print("-1")
