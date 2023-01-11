# 정수 1개 입력 받기
# number = int(input())
# print(number)

# 공백으로 구분된 여러개의 정수 입력 받기
# numbers = list(map(int,input().split()))
# print(numbers)

# 공백으로 구분된 여러개의 단어 입력 받기
# string = input().split()
# print(string)

# 공백으로 구분된 2개의 정수 입력 받기
# a, b = list(map(int,input().split()))
# print(a, b)

# 테스트 케이스 수가 주어지는 입력 받기
# T = int(input()) # 테스트 케이스 수
# for t in range(1, T+1):
#     print(t)
#     # 이하 입력 코드
#     pass

# 입력 줄 수가 주어지는 입력 받기
# N = int(input()) # 입력 줄 수
# for _ in range(N):
#     # 이하 입력 코드
#     pass

# 테스트 케이스와 입력 줄 수가 주어지는 입력 받기
# T = int(input()) # 테스트 케이스 수
# for t in range(1, T+1):
#     N = int(input()) # 입력 줄 수
    
#     for _ in range(N):
#         # 이하 입력 코드
#         pass

# 파일 입력
# # input.txt 파일을 생성하고,입력을 작성해주세요.
# # 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
# import sys
# sys.stdin = open("input.txt", "r")
# # 이하 입력 코드

# 문제 1
# 공백으로 구분된 정수
# 5 19 2901 2039 41 2 23 40 

# numbers = list(map(int,input().split()))
# print(numbers)

# 문제 2
# 공백으로 구분된 문자열
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.

# string = input().split()
# print(string)

# 문제 3
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 2 
# 3
# 1
# 2 
# 3
# 2
# 1 
# 2

# T = int(input())
# for T in range(1, T+1):
#     N = int(input())
#     for i in range(1,N+1):
#         print(i)

# 문제 4
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 2  
# 3  
# 1 1
# 2 2
# 3 3
# 2
# 1 1
# 2 2

# T = int(input())
# for T in range(1, T+1):
#      N = int(input())
#      for i in range(1,N+1):
#          print(i, i)

# 문제 5
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.
# 2 
# 2 
# L2, consectetur adipiscing elit.
# Donec rutrum ex vel nibh vulputate, ut convallis turpis elementum.
# 5
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Nam eget tellus eu tortor rutrum tincidunt.
# Etiam scelerisque lacus ut enim dignissim, nec pulvinar nisl
# Vivamus quis orci malesuada, mattis libero a, rhoncus sapien.
# Phasellus vehicula turpis a nisl ullamcorper finibus.

# T = int(input()) # 테스트 케이스 수
# for T in range(1, T+1):
#     N = int(input()) # 입력 줄 수
#     for i in range(N):
#         string = input()
#         print(string)

# 문제 6
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 2  
# 3  
# 1 3 492 32
# 32 90 65 2 1
# 3 9 9
# 2
# 1 
# 4 93 1 2

# T = int(input()) # 테스트 케이스 수
# for T in range(1, T+1):
#     N = int(input()) # 입력 줄 수
#     for i in range(N):
#         numbers = input()
#         print(numbers)

# 문제 7
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
# 2 1
# 1
# 2

# test_case,number = map(int,input().split())
# print(test_case,number)
# for i in range(test_case):
#     for j in range(number):
#         numbers = list(map(int,input().split()))
#         for n in numbers:
#             print(n,end=" ")
#         print()

# 문제 8
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
# 2 2
# 2 3
# 1 2
# 3 4
# 5 9

# test_case,number = map(int,input().split())
# print(test_case,number)
# for i in range(test_case):
#     for j in range(number):
#         numbers = list(map(int,input().split()))
#         for n in numbers:
#             print(n,end=" ")
#         print()

# 문제 9
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.
# 2 3 
# 1 3 492 
# 32 90 65
# 3 9 9
# 1 3 9
# 4 93 1
# 2 4 2

# test_case,number = map(int,input().split())
# print(test_case,number)
# for i in range(test_case):
#     for j in range(number):
#         numbers = list(map(int,input().split()))
#         for n in numbers:
#             print(n,end=" ")
#         print()