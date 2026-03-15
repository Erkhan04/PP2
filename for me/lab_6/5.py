s = input()

if any(c in 'aeoiuAEOIU' for c in s):
    print("Yes")
else:
    print('No')