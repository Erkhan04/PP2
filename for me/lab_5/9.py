import re

x = input()

c = re.findall(r'\b[A-Za-z]{3}\b',x)


print(len(c))