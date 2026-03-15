n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dot = sum(x * y for x, y in zip(arr, arr2))
print(dot)