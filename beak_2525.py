# 백준 2525번 오븐 시계 
# 2025.11.07 1회 풀이

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

