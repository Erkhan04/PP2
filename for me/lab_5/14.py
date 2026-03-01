import re

x = input()

c = re.findall(r'\w+', x)
print(len(c))