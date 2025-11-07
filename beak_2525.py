h, m = map(int, input().split())
t = int(input())

if m + t >= 60:
    h += ((m + t) // 60)
    if h >= 24:
        h %= 24
    m = ((m + t) % 60)
    print(h, m)
else:
    print(h, m + t)