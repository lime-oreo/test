wGnd = 120
hGnd = 50

wDivisor = []
hDivisor = []

maxDivisor = 0

for i in range(1, 120):
    if wGnd % i == 0:
        wDivisor.append(i)

for i in range(1, 51):
    if hGnd % i == 0:
        hDivisor.append(i)

for h in hDivisor:
    for w in wDivisor:
        if h == w:
            maxDivisor = h

print('최대 가로, 세로 길이  : ', maxDivisor)

wCnt = wGnd / maxDivisor
hCnt = hGnd / maxDivisor

print("전체 텃밭의 개수 : ", int(wCnt * hCnt))
