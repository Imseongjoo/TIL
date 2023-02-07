# 9498 시험 성적	
# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 시험 성적을 출력한다.

S = int(input())
if 90<=S:
    print("A")
elif 80<=S<=89:
    print("B")
elif 70<=S<=79:
    print("C")
elif 60<=S<=69:
    print("D")
else:
    print("F")

# 9093 단어 뒤집기	
# 문제
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

N=int(input())
for i in range(N):
    string=list(input().split())
    for j in string:
        print(j[::-1], end=' ')

# 11721 열 개씩 끊어 출력하기	
# 문제
# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

# 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어가 주어진다. 단어는 알파벳 소문자와 대문자로만 이루어져 있으며, 길이는 100을 넘지 않는다. 길이가 0인 단어는 주어지지 않는다.

# 출력
# 입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다. 단어의 길이가 10의 배수가 아닌 경우에는 마지막 줄에는 10개 미만의 글자만 출력할 수도 있다.

N = input()
for i in range(0, len(N), 10):
    print(N[i:i+10])

# 2947 나무 조각	
# 문제
# 동혁이는 나무 조각을 5개 가지고 있다. 나무 조각에는 1부터 5까지 숫자 중 하나가 쓰여져 있다. 또, 모든 숫자는 다섯 조각 중 하나에만 쓰여 있다.

# 동혁이는 나무 조각을 다음과 같은 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만들려고 한다.

# 첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
# 처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의 순서를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 조각에 쓰여 있는 수가 순서대로 주어진다. 숫자는 1보다 크거나 같고, 5보다 작거나 같으며, 중복되지 않는다. 처음 순서는 1, 2, 3, 4, 5가 아니다.

# 출력
# 두 조각의 순서가 바뀔때 마다 조각의 순서를 출력한다.

T = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]
while True:
    for i in range(len(T)-1):
        if T[i] > T[i+1]:
            T[i], T[i+1] = T[i+1], T[i]
            print(" ".join(map(str, T)))
    if T == answer:
        break

# # 나무 조각

# # 입력 문자열
# input_numbers = "2 3 4 5 1"
# input_numbers = input_numbers.split()

# # 숫자 리스트
# numbers = []

# for number in input_numbers:
#     numbers.append(int(number))

# # print(numbers)
# while True:
#     # 시작 : 0 -> 마지막 - 1 : 3
#     for i in range(0, len(numbers) -1):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

#             result = ""
#             for number in numbers:
#                 result += str(number) + " "
            
#             print(result)
    
#     if numbers == [1,2,3,4,5]:
#         break

#     # # 첫 번째 조각의 수 > 두 번째 조각의 수 ???
#     # if numbers[0] > numbers[1]:
#     #     # 조건식이 성립하면 값을 교환
#     #     numbers[0], numbers[1] = numbers[1], numbers[0]
        
#     #     result = ""
#     #     for number in numbers:
#     #         result += str(number) + " "

#     #     # 값을 확인
#     #     print(result)

#     # if numbers[1] > numbers[2]:
#     #     numbers[1], numbers[2] = numbers[2], numbers[1]
#     #     result = ""
#     #     for number in numbers:
#     #         result += str(number) + " "
#     #     # 값을 확인
#     #     print(result)

#     # if numbers[2] > numbers[3]:
#     #     numbers[2], numbers[3] = numbers[3], numbers[2]
        
#     #     result = ""
#     #     for number in numbers:
#     #         result += str(number) + " "

#     #     # 값을 확인
#     #     print(result)

#     # if numbers[3] > numbers[4]:
#     #     numbers[3], numbers[4] = numbers[4], numbers[3]
#     #     result = ""
#     #     for number in numbers:
#     #         result += str(number) + " "
#     #     # 값을 확인
#     #     print(result)

#     # if numbers == [1, 2, 3, 4, 5]:
#     #     break


# # 이중 반복문 해결할 떄
# # 처음부터 이중 반복으로 접근하면 어렵습니다.

# # 작은 단위로 문제를 해결하기 -> 알고리즘 풀이에서 중요한 팁!