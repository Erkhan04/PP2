n = int(input())
arr = list(map(int, input().split()))

s = filter(lambda x: x % 2 == 0, arr)
print(len(list(s)))
