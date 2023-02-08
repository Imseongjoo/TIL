import sys
# from pprint import pprint
sys.stdin = open("어디에 단어가 들어갈 수 있을까.txt")

# 2차원 리스트에서 하나의 행을 구분해서 출력
def pprint(arr):
    for row in arr:
        print(*row)

# 테스트케이스 수
T = int(input())

# 테스트케이스 수 만큼 순회
for t in range(1, T+1):
    # print(t)
    # 띄어쓰기로 구분된 정수 2개를 입력
    N, K = list(map(int, input().split()))
    # print(N, K)
    
    # 2차원 리스트 저장 변수
    grid = []
    
    # N x N 입력
    # N번 만큼 입력
    for _ in range(N):
        # 띄어쓰기로 구분된 정수 리스트를 입력
        temp_list = list(map(int, input().split()))
        # print(temp_list)
        grid.append(temp_list)
    
    # pprint(grid)

    # 탐색을 시작하기전에 출력 값을 초기화
    answer = 0

    # 가로 탐색
    # 열(x) -> 행(y)
    for y in range(N):
        empty_count = 0 
        for x in range(N):
            # print(f"행:{y} / 열:{x}")
            # print(grid[y][x])
            
            # K 만큼의 빈 공간이 있는지 확인

            # 흰공간(1)을 만났을 때
            if grid[y][x] == 1:
                # 빈공간의 개수를 1 증가
                empty_count += 1

            # 검은공간(0)을 만났을 때
            if grid[y][x] == 0:
                # 지금까지의 빈공간의 수가 K 확인
                if empty_count == K:
                    # 단어가 들어갈 수 있는 자리 1 증가
                    answer += 1

                # 빈공간의 수를 0 초기화
                empty_count = 0
        
        if empty_count == K:
            answer += 1

    # 세로 탐색
    # 행(y) -> 열(x) 
    for x in range(N):
        empty_count = 0 
        for y in range(N):
            # print(f"행:{y} / 열:{x}")
            # print(grid[y][x])
            
            # K 만큼의 빈 공간이 있는지 확인

            # 흰공간(1)을 만났을 때
            if grid[y][x] == 1:
                # 빈공간의 개수를 1 증가
                empty_count += 1

            # 검은공간(0)을 만났을 때
            if grid[y][x] == 0:
                # 지금까지의 빈공간의 수가 K 확인
                if empty_count == K:
                    # 단어가 들어갈 수 있는 자리 1 증가
                    answer += 1

                # 빈공간의 수를 0 초기화
                empty_count = 0
        
        if empty_count == K:
            answer += 1

    # #1 2
    print(f"#{t} {answer}")

list_ = [
    [1, 3, 3, 6, 7],
    [8, 13, 9, 12, 8],
    [4, 16, 11, 12, 6],
    [2, 4, 1, 23, 2],
    [9, 13, 4, 7, 3],
]
N = 5
M = 2

max_fly_sum = 0

# 파리채의 시작점을 찾기위한 탐색
for y in range(0, N - M + 1):
    for x in range(0, N - M + 1):
        # print(y, x)
        
        # 파리채 영역의 파리의 수
        fly_sum = 0

        # 파리채의 영역 탐색
        for ym in range(y, y + M):
            for xm in range(x, x + M):
                # 죽인 파리의 수
                fly_sum += list_[ym][xm]
        
        # 가장 많이 죽인 파리의 수 갱신
        if max_fly_sum < fly_sum:
            max_fly_sum = fly_sum

print(max_fly_sum)