enns = []
ans = []

T = int(input())

for i in range(T):
    enns.append(int(input()))

for N in enns:
    count = 0
    for t in range(1, N+1):
        if((N % t == 0) and (t % 2 == 0)):
            count += 1
    ans.append(count)

for i in ans:
    print(i)
