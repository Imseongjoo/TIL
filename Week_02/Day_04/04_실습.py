# 문제 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.
# 단, count() 함수는 사용하지마세요.

str = input("문자열을 입력하세요 > ")
list = list(str)
cnt = 0
for x in list:
    if "e" in x:
        cnt += 1
    else:
        cnt += 0
print(cnt)

# string = input("문자열을 입력하세요 > ")
# count = 0
# for char in string:
#     if char == "e":
#         count += 1

# print(count)

# 문제 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.
# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)
# 단, count() 함수는 사용하지마세요.

str = input("문자열을 입력하세요 > ")
list = list(str)
cnt = 0
for x in list:
    if "a" in x:
        cnt += 1
    elif "A" in x:
        cnt += 1
    elif "e" in x:
        cnt += 1
    elif "E" in x:
        cnt += 1
    elif "i" in x:
        cnt += 1
    elif "I" in x:
        cnt += 1
    elif "o" in x:
        cnt += 1
    elif "O" in x:
        cnt += 1  
    elif "u" in x:
        cnt += 1
    elif "U" in x:
        cnt += 1 
    else:
        cnt += 0
print(cnt)

# string = input("문자열을 입력하세요 > ")
# count = 0
# for char in string:
#     if (
#         char == "e"
#         or char == "E"
#         or char == "a"
#         or char == "A"
#         or char == "i"
#         or char == "I"
#         or char == "o"
#         or char == "O"
#         or char == "u"
#         or char == "U"
#     ):
#         count += 1

# print(count)

# 문제 3
# 입력과 같은 딕셔너리 변수가 있을 때, 
# 해당 인물의 나이를 출력하세요.

# 입력
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

### 이하 문제 해결 코드 작성
dict_variable["나이"] = 30
print(f'나이 : {dict_variable["나이"]}세')

# dict_variable = {
#     "이름": "정우영",
#     "생년": "2000",
#     "회사": "하이퍼그로스",
# }

# dict_variable["나이"] = 2023 - int(dict_variable["생년"]) + 1

# print(dict_variable["나이"])

# 문제 4
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고,
# 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

dict_variable = {
    "이름": input("이름을 입력하세요 > "),
    "전화번호": input("전화번호를 입력하세요 >"),
    "거주지": input("거주지를 입력하세요 > "),
}
for key in dict_variable:
    print(f"{key} : {dict_variable[key]}")

# name = input("이름을 입력하세요 > ")
# phone_number = input("전화번호를 입력하세요 > ")
# residence = input("거주지를 입력하세요 > ")
# dict_variable = {
#     "이름": name,
#     "전화번호": phone_number,
#     "거주지": residence,
# }
# print(dict_variable)
# for key, value in dict_variable.items():
#     print(f"{key} : {value}")

# 문제 5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 
# 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
# Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다

name = input("이름을 입력하세요 > ")
number = input("전화번호를 입력하세요 > ")
email = input("이메일을 입력하세요 > ")
live = input("거주지를 입력하세요 > ")

dict_variable = {
    name :
    {"전화번호": number,
    "이메일": email,
    "거주지": live}
}   
print(dict_variable)

# name = input("이름을 입력하세요 > ")
# phone_number = input("전화번호를 입력하세요 > ")
# email = input("이메일을 입력하세요 > ")
# residence = input("거주지를 입력하세요 > ")

# dict_variable = {
#     name: {
#         "전화번호": phone_number,
#         "이메일": email,
#         "거주지": residence,
#     }
# }
# print(dict_variable)

# 출력 예시
# 이름을 입력하세요 > 정우영
# 전화번호를 입력하세요 > 010-1234-5678
# 이메일을 입력하세요 > beemo@hphk.kr 
# 거주지를 입력하세요 > 서울시 
# {'정우영': {'전화번호': '010-1234-5678', '이메일': 'beemo@hphk.kr', '거주지': '서울시'}}

# 문제 6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello 
# h 1
# e 1
# l 2
# o 1

str = input("문자열을 입력하세요 > ")
dic = {}
char = []
for char in str:
        try: dic[char] += 1
        except: dic[char] = 1
print(dic)

# string = input("문자열을 입력하세요 > ")
# dict_variable = {}
# for char in string:
#     if char in dict_variable.keys():
#         dict_variable[char] += 1
#     elif char not in dict_variable.keys():
#         dict_variable[char] = 1

# for key, value in dict_variable.items():
#     print(key, value)