# 정수 1개 입력 받기
number = int(input('a'))
print(number)

# 공백으로 구분된 여러개의 정수 입력 받기
numbers = list(map(int,input(['정수들']).split()))
print(numbers)

# 공백으로 구분된 여러개의 단어 입력 받기
string = input('문자열').split()
print(string)

# 공백으로 구분된 2개의 정수 입력 받기
a, b = list(map(int,input(['정', '수']).split()))
print(a, b)

# 문제 1
# 5 # 1

# 문제 2
# 2 5 # 4

# 문제 3
# 1 2 3 # 2

# 문제 4
# word1 word2 word3 #3

# 문제 5
# 1 2 3 4 5 # 2

# 문제 6
# -10 10 # 4

# 문제 7
# a b c d e # 3

# 문제 8
# 3 17 1 39 8 41 2 32 99 2 # 2

# 문제 9
# 1 4 0 10 2 3 9 # 2