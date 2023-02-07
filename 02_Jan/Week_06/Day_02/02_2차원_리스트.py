a = [1, 2, 3, 4, 5]
N = len(a)

# [1, 2, 3, 4, 5]
# n == 1 : [2, 3, 4, 5, 1]
# n == 2 : [3, 4, 5, 1, 2]

new_a = [None for _ in range(N)]
print(a, new_a)

for i in range(N):
    # 새로운 리스트에 
    new_a[i-5] = a[i]
    print(new_a)

# n == 1 : [5, 1, 2, 3, 4]
# n == 2 : [4, 5, 1, 2, 3]
n = 2
new_a = [None for _ in range(N)]
print(a, new_a)
for i in range(N):
    # 새로운 리스트에 
    print((i+n)%N)
    new_a[(i+n)%N] = a[i]
    print(new_a)

for n in range(5):
    print(a[-n:] + a[:-n])

from collections import deque 

a = [1, 2, 3, 4, 5]
d = deque(a)
d.rotate(2)
print(d)

a = [1, 2, 3, 4, 5]
d = deque(a)
d.rotate(-2)
print(d)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 0, 1]
]

print(matrix)
# 1. 행 우선 순회
N = len(matrix)
M = len(matrix[0])

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()
print('=====================')
# 리스트로 볼 수도 있다.. 하지만 지금은 인덱스!
for i in range(N):
    for n in matrix[i]:
        print(n, end=" ")
    print()
print('=====================')

# 2. 열 우선 순회
for i in range(M):
    for j in range(N):
        print(matrix[j][i], end=" ")
    print()

# 3. 총합
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 0, 1]
]

N = len(matrix)
M = len(matrix[0])

# 방법 1.
count = 0
for i in range(N):
    for j in range(M):
        count += matrix[i][j]
print(count)

# 방법 2. 
count = 0
for elem in matrix:
    # [1, 2, 3, 4], ...... 
    count += sum(elem)
print(count)

# 방법 3. 
# 각 요소에 sum한 결과를 모아서 sum...?
print(sum(map(sum, matrix)))

# Q. 각 행별 합을 구하는 코드를 작성하시오. 