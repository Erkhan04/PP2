import re

x = input()

c = re.compile(r'\b\w+\b')
d = c.findall(x)

print(len(d))