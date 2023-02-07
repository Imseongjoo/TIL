matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(list(zip(*matrix)))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
# [
#     (1, 4, 7), 
#     (2, 5, 8), 
#     (3, 6, 9)
# ]

print(list(zip(*matrix[::-1])))
# [
#     (7, 4, 1), 
#     (8, 5, 2), 
#     (9, 6, 3)
# ]

N = 5
M = 21

# O(N^3)
for i in range(5):
    for j in range(5):
        for k in range(5):
            # i, j, k => 비교문 필요 
             pass

# O(N^3)
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            pass 
        
# (1, 1)
# 위와 같은 조합이 들어왔을 때 상하좌우를 모두 출력하는 코드!

# 상 (i-1, 0)
# 하 (i+1, 0)
# 좌 (0, j-1)
# 우 (0, j+1)

x = 0 
y = 0
print(x, y)

# 상하좌우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dx, dy in delta:
    print(x + dx, y + dy)