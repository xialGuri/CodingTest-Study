N, r, c = map(int, input().split())

count = 0
while N != 0:
    N -= 1
    size = 2 ** N

    # 1사분면
    if r < size and c < size:
        count += 0

    # 2사분면
    elif r < size and c >= size:
        count += size * size
        c -= size

    # 3사분면
    elif r >= size and c < size:
        count += size * size * 2
        r -= size

    # 4사분면
    else:
        count += size * size * 3
        r -= size
        c -= size

print(count)


