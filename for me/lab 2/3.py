x = int(input())
num = list(map(int, input().split()))

s = 0
for i in range(x):
    s += num[i]

print(s)