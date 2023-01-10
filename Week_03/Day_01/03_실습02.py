# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.
# 단, index() / find() 메서드는 사용하지마세요.

# 출력 예시1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1

# str = input('문자열을 입력하세요 > ')
# i = ''
# cnt = 0
# for i in str:
#     if 'e' not in str:
#             print(int(-1))
#             break
#     elif 'e' not in i:
#             cnt += 1     
#     elif 'e' in i:
#             print(int(cnt))
       
# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# hello 1

# str = input('문자열을 입력하세요 > ').split()
# print(len(str))

# 문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple # 사용자 입력
# appl

# x = input("문자열을 입력하세요 > ")
# num = x.index('e')
# strx = x[:num] + x[num+1:]
# print(strx)

# 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고, 
# 문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple p # 사용자 입력
# 2

# a, b = input('문자열 알파벳').split()
# i = ''
# cnt = 0
# for i in a:
#     if b in i:
#             cnt += 1     
#     elif b in i:
#             cnt = 0
# print(int(cnt))

# 문제 5
# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > 010 1234 5678 # 사용자 입력
# 010-1234-5678

# a = int(input('자연수를 입력하세요 > '))
# b = int(input('자연수를 입력하세요 > '))
# c = int(input('자연수를 입력하세요 > '))
# k = str(a)+'-'+str(b)+'-'+str(c)
# print(k)

# 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > 244 # 사용자 입력
# 10

n =  int(input())
result =0

while n > 0:
    result += n%10
    n //= 20

print(result)