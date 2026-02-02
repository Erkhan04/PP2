x = int(input())
if x < 1:
    print("NO")
else:
    while x % 2 == 0:
        x //= 2
    
    if x == 1:
        print("YES")
    else:
        print("NO")