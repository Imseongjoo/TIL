number_list = [1, 2, 3, 4, -5]

# result : 0
result = 0
# number_list를 반복해서 number
for number in number_list:
    # number를 result에 더함
    result = result + number
print(result)

# 다이얼
# 딕셔너리 활용

dict_ = {
    'A': 3,
    'B': 3,
    'C': 3,
    'D': 4,
    'E': 4,
    'F': 4,
}

input_string = 'WA'

# 회사에 있는 사람
# 그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
# enter / leave
# 현재 사람의 상태가 enter -> 회사에 있음.

"""
4
Baha enter
Askar enter
Baha leave
Artem enter
"""
# input_list = [
#     "Baha enter",
#     "Askar enter",
#     "Baha leave",
#     "Artem enter"
# ]

# # 사람의 상태를 기록할 변수
# log_dict = {}

# n = 4
# for i in range(n): # n 만큼 출입 기록 입력
#     # name, log = input_list[i]
#     # print(input_list[i])
#     name, log = input_list[i].split()
#     # print(name,log)

#     # 사람의 상태(출입) 기록
#     # key(사람) - value(출입 상태)
#     log_dict[name] = log

# # print(log_dict)

# # 현재 사람의 상태가 enter만 남긴다.

# # 남긴다 -> enter 리스트에 저장한다.
# enter_name_list = []

# # 이름과 출입 상태를 함께 순회
# for name, log in log_dict.items():
#     if log == "enter":
#         # 저장
#         enter_name_list.append(name)

# # print(enter_name_list)

# # # sorted() 정렬 함수
# enter_name_list = sorted(enter_name_list,reverse=True)

# for name in enter_name_list:
#     print(name)

dict_ = {
    3: ['x', 'cc'],
    1: ['x', 'aa'],
    2: ['x', 'bb'],
}

# print(dict_)
print(dict_.items())

A_sorted = sorted(dict_.items(), key=lambda x: -x[0])
print(A_sorted)

B_sorted = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
print(B_sorted)

C_sorted = sorted(dict_.items(), key=lambda x: x[1][1])
print(C_sorted)

# 예시
# 6471-6836-9525-5276

card_number = "6471-6836-9525-5276"

# 습관
# 정수를 입력받으면 무조건 int()
# - 지우고 나머지 int()

# - 지우기
card_number = card_number.replace("-", "")
print(card_number)

"""
1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
2. 카드 번호에 "-"이 들어갈 수 있으며 
"-" 를 제외한 숫자의 개수는 16개이다.
"""

if len(card_number) == 16:
    print("카드 번호 규칙 2를 만족합니다.")

    # card_number[0] == 3 4 5 6 9
    if card_number[0] in "34569":
        print('카드 번호 규칙 1을 만족합니다.')

        # 카드 번호
        print('현재 숫자 나열은 카드 번호 입니다.')

else:
    print("카드 번호가 아닙니다.")

# 요구 조건에 맞는 코드를 구현
# 너무 규칙 순서에 따를 필요는 없다.

"""
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 
여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
다음과 같은 수 분포가 있으면,
10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
최빈수는 8이 된다.
최빈수를 출력하는 프로그램을 작성하여라.
(단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
"""

number_list = [10, 1, 9, 9, 9, 2, 8, 8, 4, 9, 10, 8, 3]

# 숫자 개수 카운팅을 위한 딕셔너리
number_dict = {}

for number in number_list:
    # 숫자(number)가 딕셔너리의 키(Key)
    if number in number_dict.keys():
        number_dict[number] += 1

    # 숫자(number)가 딕셔너리의 키(Key)가 아닐 때
    elif number not in number_dict.keys():
        # 아닐 때 어떤 로직이 필요할까요?
        # 처음 등장한 숫자기 때문에 1로 초기화
        number_dict[number] = 1

# 숫자 개수 확인
# print(number_dict)

# 최빈수를 어떻게 찾을까?
# 최빈수가 몇인지를 우리는 저장해야합니다.
max_count = 0

# 최빈수에 해당하는 점수를 저장할 변수
result_score = 0

# print(number_dict.items())
# 키(숫자) - 값(개수)
for score, count in number_dict.items():
    # print(score, count)
    # 개수(count)가 현재까지의 최빈수(max_count)도 많다면
    if count > max_count:
        max_count = count
        result_score = score

    # 개수(count)가 현재 최빈수와 동일한 경우
    if count == max_count:
        # 현재 점수(score)가 현재 최빈수 점수보다 클 때
        if score > result_score:
            # 현재 정답 점수 갱신
            result_score = score

print(result_score)

# 이 문제에서 우리가 배워야할 점? 얻어야할 점? 얻어야할 스킬?
# 반복문 내부에서 값을 변화
# 하나의 값이 아니라 두 개 이상의 값을 변화(갱신)

# 숫자 리스트가 있을 때 가장 큰 숫자와 그 숫자의 위치(index)는?
