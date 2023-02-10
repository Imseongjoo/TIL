# 1208 [S/W 문제해결 기본] 1일차 - Flatten

for i in range(1, 11) :
    N = int(input())
    box = list(map(int, input().split()))
    for j in range(N) :
        max_index = box.index(max(box))
        min_index = box.index(min(box))
        box[max_index] -= 1
        box[min_index] += 1
    print(f"#{i} {max(box)-min(box)}")