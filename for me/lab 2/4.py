x = int(input())
num = list(map(int, input().split()))

s = 0
for i in range(x):
    if num[i] > 0:
        s += 1

print(s)