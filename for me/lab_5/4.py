import re

x = input()

c = re.findall(r"\d", x)
print(" ".join(c))