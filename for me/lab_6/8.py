n = int(input())
a = list(map(int, input().split()))

dot = sorted(set(a))
print(*dot)