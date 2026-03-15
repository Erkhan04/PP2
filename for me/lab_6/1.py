n = int(input())
arr = list(map(int, input().split()))

s = map(lambda x: x**2, arr)
print(sum(s))
