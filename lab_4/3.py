def s(n):
    for i in range(n, b + 1 ):
            yield i * i


n, b = map(int, input().split())
for num in s(n):
    print(num)
