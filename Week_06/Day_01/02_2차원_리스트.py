N = 4
M = 3

matrix = [[0] * M] * N 
print(matrix)
matrix[0][0] = 1
print(matrix)

print('====================')

matrix2 = [[0] * M for _ in range(N)]
print(matrix2)
matrix2[0][0] = 1
print(matrix2)

# 리스트 복사
a = [1, 2, 3]
b = list(a) # a[:]
a[0] = 100

# deepcopy

import pprint
# 1. 손수 만들기
# matrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# 2. for문 활용 
# print([0] * 10)
# 4X3 행렬 만든다고 하면
N = 4 # 행
M = 3 # 열

matrix = []
for _ in range(N):
    # [0, 0, 0, ... 0] 
    matrix.append([0] * M)

pprint.pprint(matrix)

# 3. 리스트 컴프리헨션
# 반복하면서 append 특정 값을 할 때
# 어떠한 요소로 구성된 리스트 만들 때 

matrix = [[0] * M for _ in range(N)]
pprint.pprint(matrix)

# 1. 8 * 8
# text = '.F.F...F'
# # 어떻게 바꾼다?
# # ['.', 'F', '.', ..., 'F']
# list(text)

import pprint

# 1-1. 반복문
matrix = []
for _ in range(8):
    # text = '.F.F...F'
    matrix.append(list(input()))

pprint.pprint(matrix)

# 1-2. list comprehension
# line = '.F.F...F'
matrix = [list(input()) for _ in range(8)]

# 2. 3X3
# line = '1 2 3'
# [1, 2, 3]
matrix = [list(map(int, input().split())) for _ in range(3)]

# matrix = []
# for _ in range(3):
#     matrix.append(__________________)