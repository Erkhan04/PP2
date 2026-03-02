import re

x = input()

c = re.compile(r'^\d+$', )
if c.match(x):
    print('Match')
else:
    print('No match')