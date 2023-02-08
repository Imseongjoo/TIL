f = open('01.txt', 'r', encoding='UTF8')
text = f.read()
print(text)

# string_list = [
#     'Hello, Python!',
#     '1일차 파이썬 공부 중',
#     '2일차 파이썬 공부 중',
#     '3일차 파이썬 공부 중',
#     '4일차 파이썬 공부 중',
#     '5일차 파이썬 공부 중',
# ]

# with open('./01.txt', 'w') as f:
#     for string in string_list:
#         f.write(string + '\n')