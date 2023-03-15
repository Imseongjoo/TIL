target_number = int(input())
n = 0
result = 0
# 조건 : target_number >= n
# 반복 때마다 n+=1, result 더하기!

while target_number >= n:
    result += n
    n += 1
    # print(result, n)
print(result)

# for의 기본!
# 반복가능한 객체...
# 숫자통
target_number = int(input())
result = 0

for n in range(1, target_number+1):
    result = n + result

print(result)
