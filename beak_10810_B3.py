# 백준 10810번 (2025.11.10 풀이)


# 슬라이싱을 활용한 풀이 1
n, m = map(int, input().split())

lst = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    lst[i - 1 : j] = [k] * (j - i + 1)
    
print(" ".join(map(str, lst)))
# 슬라이싱은 [start:end:step]


# 반복문 만을 활용한 풀이 2
n, m = map(int, input().split())
box = [0] * n

for _ in range(m) :
    i, j, k = map(int, input().split())
    
    for idx in range(i, j + 1):
        box[idx - 1] = k

for i in range(n):
    print(box[i], end=' ')

# end=' ' 공백을 기준으로 줄바꿈 없이 출력