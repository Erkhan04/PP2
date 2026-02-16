n = int(input())
if n <= 1:
    print("NO")
else:
    is_Prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_Prime = False
            break
    if is_Prime:
        print("YES")
    else:
        print("NO")
        