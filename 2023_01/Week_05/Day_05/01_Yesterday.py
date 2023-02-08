
N = 8
list_ = [12, 20, 1, 3, 4, 4, 11, 1]

# 가장 큰 오르막길 길이를 저장할 변수
max_length = 0

# 첫 번째 숫자(오르막길의 시작 높이)
start = 0

# 마지막 숫자(오르막길의 끝 높이)
end = 0

for i in range(1, N):
    # 뒷 숫자가 앞 숫자보다 큰가요?
    # 오르막길인가요?
    if list_[i] > list_[i-1]:
        # 오르막길 구간

        # start가 0 일 때 
        # 오르막길이 시작을 하지 않았을 때
        # start(시작)을 저장
        if start == 0:
            start = list_[i - 1]

        # 마지막 인덱스도 오르막길일 때
        if i == N - 1:
            end = list_[i]
            length = end - start

            if max_length < length:
                max_length = length

    # 오르막길이 끝이날 때
    elif list_[i] <= list_[i-1]:
        # 오르막길이 시작했는지 확인
        # start != 0 ?
        if start != 0:
            end = list_[i-1]
            
            # 오르막길의 길이
            length = end - start

            if max_length < length:
                max_length = length

            # 새로운 오르막길의 시작을 위해서
            start = 0

print(max_length)

# 가장 작은 값이 index = 0 위치하는 자료구조
from heapq import *

string = "mobitel"

N = len(string)

# string_list = []

string_heap = []

# i 와 j 를 순회하는 이중 for문
for i in range(1, N - 1):
    for j in range(i + 1, N):
        a = string[0:i]
        b = string[i:j]
        c = string[j:N]

        # print(a,b,c)

        reversed_a = a[::-1]
        reversed_b = b[::-1]
        reversed_c = c[::-1]

        join_string = reversed_a + reversed_b + reversed_c

        # 사전적으로 가장 앞에 나오는 단어는 무엇인가요?
        # 모든 합친 문자열을 하나의 리스트에 다 저장
        # string_list.append(join_string)
        heappush(string_heap, join_string)
    
# bometil
# 리스트에 저장된 값 중 가장 작은 값 출력
# print(min(string_list))
print(heappop(string_heap))