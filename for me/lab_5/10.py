import re

x = input()

if re.search(r'cat|dog', x):
    print("Yes")
else:
    print("No")

