n, m = map(int, input().split())
box = []

for i in range(1, n + 1):
    box.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    box[i-1:j] = box[i-1:j][::-1]
    
print(" ".join(map(str, box)))

# box[i-1:j] = box[i-1:j][::-1]
# i-1 ~ j 까지를 슬라이싱 한 후 ::-1 뒤집어라


# 슬라이싱
# list[start:end:step]
# list[1:4:1]의 의미는 [1][2][3]이렇게 가는거고
# list[4:1:-1]의 의미는 [3][2][1]이렇게 가는거다 
# 즉 start > end 이면 step < 0이 가능이고 
# start < end 이면 step > 0이 가능이다