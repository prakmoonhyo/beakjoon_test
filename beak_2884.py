# 백준 2884 알람시계

# 2025.11.07 풀이
# H, M = map(int, input().split())

# if M - 60 > 0:             cf) M - 60 은 항상 음수이거나 0 이다. 따라서 이 블록은 실행되지 않는다.
#     print(H, (M - 45))       
# elif M - 60 < 0:
#     if H == 0:
#         H = 24
#         print(H - 1, (60 - 45 + M))
#     elif H != 0:
#         print(H - 1, (60 - 45 + M))
        
H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
else:
    H -= 1
    if H < 0:
        H = 23
    print(H, M + 60 - 45)
    
# 조건이 0 <= H <= 23, 0 <= M <= 59니까 
# M - 45가 음수인지 아닌지만 판단하면 됨
    


