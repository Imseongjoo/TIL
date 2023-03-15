# 11856 반반

TC = int(input())
for _ in range(1, TC+1):
    string = list(map(str, input()))
    result = 0
    for i in range(4):
        cnt = 0
        for j in range(4):
            if string[i] == string[j]:
                cnt += 1
        if cnt == 2:
            result += 1
    if result == 4:
        print(f"#{_} Yes")
    else:
        print(f"#{_} No")
