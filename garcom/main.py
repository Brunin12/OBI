n_bandejas = int(input())
if 1 > n_bandejas or n_bandejas > 100:
    exit()
copos_quebrados = 0


for i in range(n_bandejas):
    bandeja = list(map(int, input().split()))
    if any(item < 0 or item > 100 for item in bandeja):
        exit()

    if bandeja[0] > bandeja[1]:
        copos_quebrados += bandeja[1]
print(copos_quebrados)