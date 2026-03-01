import re

x = input()

c = re.search(r'\S+@\S+\.\S+', x):
if c:
    print(c.group())
else:
    print("No email")