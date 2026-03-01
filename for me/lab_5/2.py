import re

x = input()
y = input()

if re.search(y, x):
    print("Yes")
else:
    print("No")
