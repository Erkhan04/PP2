import re

x = input()

c = re.findall(r'\d{2}/\d{2}/\d{4}/', x)
print(len(c))