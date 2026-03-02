import re

x = input()

c = re.search(r'Name:\s*(.+),\s*Age:\s*(\d+)', x)
if c:
    print(c.group(1), c.group(2))