import re

x = input()

def dou(a):
    d = a.group()
    return d * 2

c = re.sub(r'\d', dou, x)
print(c)