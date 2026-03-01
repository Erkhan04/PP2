import re

x = input()

c = re.findall(r'[A-Z]',x)


print(len(c))