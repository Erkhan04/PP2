x = int(input())
num = list(map(int, input().split()))

s = num[0]
for i in range(1, x):
    if num[i] > s:
        s = num[i]
        x = i + 1

print(x)