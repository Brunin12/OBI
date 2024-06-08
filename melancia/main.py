peso = int(input())

if 1 > peso | peso > 100:
    exit()

if peso % 2 == 0 and peso > 2:
    print("YES")
else:
    print("NO")
