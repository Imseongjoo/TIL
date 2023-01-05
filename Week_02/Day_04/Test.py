str = input("문자열을 입력하세요 > ")
dic = {}
char = []
for char in str:
        try: dic[char] += 1
        except: dic[char] = 1
print(dic)

# str = input("문자열을 입력하세요 > ")
# dic = {}
# for chr in str:
#         if chr in dic:
#               dic[chr] += 1
#         else :
#               dic[chr] = 1
# print(dic)