import re

x = input()

if re.match(r'^[A-Za-z].*[0-9]$', x):
    print("Yes")
else:
    print("No")