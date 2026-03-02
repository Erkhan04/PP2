import re

x = input()
y = input()
c = re.findall(re.escape(y), x)
print(len(c))