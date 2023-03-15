# 1288 새로운 불면증 치료법

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ls = [0]*10
    i = 0
    while (True):
        if 0 not in ls:
            break
        else:
            i += 1
            num = str(N*i)
            for j in range(len(num)):
                ls[int(num[j])] = 1
    print("#{} {}".format(test_case, num))
