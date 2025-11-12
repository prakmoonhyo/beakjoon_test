# lst = []
# for i in range(10):
#     lst.append(int(input()) % 42)
    
# print(len(set(lst)))
        
lst = []
for _ in range(10):
    lst.append(int(input()) % 42)

unique = []
for i in lst:
    if i not in unique:
        unique.append(i)

print(len(unique))
