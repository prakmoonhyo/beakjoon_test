# 백준 10871번 (2025.11.09 풀이)
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.


# 풀이 1
n, x = map(int, input().split())
lst = list(map(int, input().split()))
min_lst = []

for i in lst:
    if i < x:
        min_lst.append(i)

print(*min_lst) # 자동으로 공백 기준 출력 해줌 

# join을 이용한 풀이 2

# words = ["apple", "banana", "cherry"]
# result = " ".join(words) 이때 join은 문자열만 가능
# print(result)

# apple banana cherry

# 따러서 리스트에 정수 형태를 출력 하려면 
# " ".join(map(str, lst)) 형태를 사용

n, x = map(int, input().split())
lst = list(map(int, input().split()))
min_lst = []

for i in lst:
    if i < x:
        min_lst.append(i)


print(" ".join(map(str, min_lst)))
# " "을 기준으로 출력해준다.
