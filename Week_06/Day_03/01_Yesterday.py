# https://www.acmicpc.net/problem/9455
# 백준 9455 박스

grid = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 1],
    [1, 1],
]

m = 5  # 세로(행)
n = 2  # 가로(열)

# 탐색 방향은???????
# 행 우선 -> y축을 먼저 움직여야하는지
# 열 우선 -> x축을 먼저 움직여야하는지

# 박스 이동
move_dis = 0

for x in range(n):
    for y in reversed(range(m)) :
        # print(y, x, grid[y][x])

        # 박스를 이동시키기위해
        # 박스를 찾자!
        if grid[y][x] == 1:
            # 조건이 만족하면
            # 박스를 이동
            while True:
                # 조건을 작성할 때
                # 최우선 순위는
                # 범위를 체크하는 것

                # 조건 1를 만족하는지?
                # 다음 위치가 범위를 벗어나면 박스 이동 X
                if y+1 == m:
                    break

                # 조건 2을 만족하는지?
                # 다음 위치에 박스가 있을 때 박스 이동 X
                if grid[y+1][x] == 1:
                    break
                
                # 현재 위치는 비우고,
                grid[y][x] = 0

                # 다음 위치로 박스가 이동
                grid[y+1][x] = 1

                # 박스 이동 거리 + 1
                move_dis += 1

                # 다음 위치 탐색
                y += 1

# def pprint(arr):
#     for a in arr:
#         print(*a)

# pprint(grid)
print(move_dis)

# https://www.acmicpc.net/problem/1652
# 백준 1652 누울 자리를 찾아라

grid = [
    ['.', '.', 'X', '.'],
    ['.', 'X', '.', '.'],
    ['X', '.', '.', '.'],
    ['.', '.', '.', '.'],
]
N = 4

# 가로로 누울 수 있는 자리 수
row_count = 0
for y in range(N):

    # 비어있는 공간 수
    empty_count = 0

    # 좌 -> 우 행 탐색
    for x in range(N):
        # 현재 탐색 좌표가 빈 공간 O
        if grid[y][x] == '.':
            empty_count += 1

        # 현재 탐색 좌표가 빈 공간 X
        if grid[y][x] == 'X':
            # 이전까지 빈 공간의 수가 2 이상이면
            if empty_count >= 2:
                # 누울 수 있는 자리 수 증가
                row_count += 1

            # 빈 공간의 수 초기화
            empty_count = 0

    # 이전까지 빈 공간의 수가 2 이상 이면
    if empty_count >= 2:
        row_count += 1

col_count = 0
for x in range(N):
    empty_count = 0
    for y in range(N):
        if grid[y][x] == '.':
            empty_count += 1

        if grid[y][x] == 'X':
            if empty_count >= 2:
                col_count += 1
            empty_count = 0

    if empty_count >= 2:
        col_count += 1

print(row_count, col_count)