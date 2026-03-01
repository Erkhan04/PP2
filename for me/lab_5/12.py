import re

x = input()

c = re.findall(r'\d{2,}', x)
print(" ".join(c))