x = int(input())
num = list(map(int, input().split()))

mx = max(num)
mn = min(num)

for i in range(x):
    if num[i] == mx:
        num[i] = mn

print(*num)