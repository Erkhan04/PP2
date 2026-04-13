n = int(input())
k = input().split()
v = input().split()

d = dict(zip(k, v))

q = input()
print(d.get(q, "Not found"))