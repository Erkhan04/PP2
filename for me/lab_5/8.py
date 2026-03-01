import re

x = input()
y = input()

c = re.split(y, x)

print(','.join(c))