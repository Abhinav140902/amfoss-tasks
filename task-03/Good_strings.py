N = int(input())
s = input() 
ones = 0
zeros = 0
for i in s:
    if(i == '1'):
        ones = ones+1
    else:
        zeros = zeros+1
if(ones!=zeros):
    print(1)
else:
    print(2)
