# 2441 별 찍기 - 4
# 문제
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(input())
for i in range(1,1+N):
    print(" "*(i-1) + "*"*(N-i+1))

# 2592 대표값
# 문제
# 어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30, 20, 60, 30, 40, 50의 평균은 (10 + 40 + 30 + 60 + 30 + 20 + 60 + 30 + 40 + 50) / 10 = 370 / 10 = 37이 된다.

# 평균 이외의 또 다른 대표값으로 최빈값이라는 것이 있다. 최빈값은 주어진 수들 가운데 가장 많이 나타나는 수이다. 예를 들어 10, 40, 30, 60, 30, 20, 60, 30, 40, 50이 주어질 경우, 30이 세 번, 40과 60이 각각 두 번, 10, 20, 50이 각각 한 번씩 나오므로, 최빈값은 30이 된다.

# 열 개의 자연수가 주어질 때 이들의 평균과 최빈값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 열 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 주어지는 자연수는 1,000 보다 작은 10의 배수이다.

# 출력
# 첫째 줄에는 평균을 출력하고, 둘째 줄에는 최빈값을 출력한다. 최빈값이 둘 이상일 경우 그 중 하나만 출력한다. 평균과 최빈값은 모두 자연수이다.

N = [int(input()) for i in range(10)]
print((round(sum(N)/10)), max(N, key = N.count))

# 10798 세로 읽기
# 문제
# 아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다. 

# 이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다. 

# A A B C D D
# a f z z 
# 0 9 1 2 1
# a 8 E W g 6
# P 5 h 3 k x
# <그림 1>

# 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다. 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다. 

# 심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다. 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다. 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다. 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다. 

# 그림 1에서 영석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:

# Aa0aPAf985Bz1EhCz2W3D1gkD6x

# 칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

# 입력
# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.

# 출력
# 영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 

a = [[0] * 15 for i in range(5)]
for i in range(5):
    ls = list(input())
    l = len(ls)
    for j in range(l):
        a[i][j] = ls[j]
for i in range(15):
    for j in range(5):
        if a[j][i] == 0:
            continue
        else:
            print(a[j][i], end='')

# 9455 박스	
# 문제
# m행 n열로 이루어진 그리드가 주어진다. 일부 칸에는 박스가 들어 있다. 모든 박스가 더 이상 움직일 수 없을 때 까지 아래로 움직인다면, 박스는 쌓여진 상태가 된다.

# 그림 (a)의 그리드의 크기는 5행 4열이고, 7칸에는 박스가 들어있다. 모든 박스가 계속해서 아래로 움직이면, 그림 (b)와 같이 변하게 된다.


# 박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다. 예를 들어, 맨 왼쪽 열에서 가장 위에 있는 박스가 움직인 거리는 2이다. 모든 박스가 이동한 거리 (각 박스가 이동한 거리의 합) 을 구하는 프로그램을 작성하시오. 위의 예제에서 박스 7개가 움직인 거리는 8이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다. (1 ≤ m, n ≤ 100) 다음 m개 줄에는 그리드의 각 행의 정보를 나타내는 n개의 정수가 주어진다. 그리드 첫 행부터 마지막 행까지 순서대로 주어진다. 박스가 들어있는 칸은 1로, 다른 칸은 0으로 주어진다. 각 정수 사이에는 공백이 하나 주어진다.

# 출력
# 각 테스트 케이스마다 입력으로 주어진 그리드에서 모든 박스가 이동한 거리를 출력한다.

for _ in range(int(input())):   
    m, n = map(int, input().split())
    box = [[] for _ in range(n)]
    for i in range(m):
        a = list(input().split())
        for j in range(n):
            box[j].append(a[j])
    move = 0
    for i in range(n):
        num = box[i].count('1')
        floor = m-1

        for j in range(m-1, -1, -1):
            if box[i][j] == '1':
                move += floor-j
                floor -= 1
    print(move)

# 1652 누울 자리를 찾아라	
# 문제
# 일 년 동안 세계일주를 하던 영식이는 여행을 하다 너무 피곤해서 근처에 있는 코레스코 콘도에서 하룻밤 잠을 자기로 하고 방을 잡았다.

# 코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다. 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 영식이가 누울 수 있는 자리에는 조건이 있다. 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다. 가로로 누울 수도 있고 세로로 누울 수도 있다. 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다. (중간에 어정쩡하게 눕는 경우가 없다.)

# 만약 방의 구조가 위의 그림처럼 생겼다면, 가로로 누울 수 있는 자리는 5개이고, 세로로 누울 수 있는 자리는 4개 이다. 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 방의 크기 N이 주어진다. N은 1이상 100이하의 정수이다. 그 다음 N줄에 걸쳐 N개의 문자가 들어오는데 '.'은 아무것도 없는 곳을 의미하고, 'X'는 짐이 있는 곳을 의미한다.

# 출력
# 첫째 줄에 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력한다.

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))
width = 0
length = 0
for x in range(n):
    cnt1 = 0
    for y in range(n):
        if matrix[x][y] == '.': 
            cnt1 += 1
        else:
            if cnt1 >= 2:
                width += 1
            cnt1 = 0
    if cnt1 >= 2 : width += 1
for z in range(n):
    cnt2 = 0
    for w in range(n):
        if matrix[w][z] == '.': 
            cnt2 += 1
        else:
            if cnt2 >= 2:
                length += 1
            cnt2 = 0
    if cnt2 >= 2 : length += 1
print(width, length)