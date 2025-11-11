# 백준 10807번
# 2025.11.08 1회 풀이
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 풀이 1

n = int(input())
lst = list(map(int, input().split()))
v = int(input())

cnt = 0

for i in lst:
    if v == i:
        cnt += 1

print(cnt)


# 풀이 2
# count : python 리스트 내장 메소드 count() 는 매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환해줍니다.

n = int(input())
n_list = list(map(int, input().split()))
v = int(input())


print(n_list.count(v))
