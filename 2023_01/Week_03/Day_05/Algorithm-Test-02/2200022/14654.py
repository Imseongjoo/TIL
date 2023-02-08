# 14654 신용카드 만들기 2

T = int(input())
for i in range(T):
    S = input()
    K = S.replace('-', '')
    if K.startswith('3') and len(K) == 16:
        print(f"#{i+1} {1}")
    elif K.startswith('4') and len(K) == 16:
        print(f"#{i+1} {1}")
    elif K.startswith('5') and len(K) == 16:
        print(f"#{i+1} {1}")
    elif K.startswith('6') and len(K) == 16:
        print(f"#{i+1} {1}")
    elif K.startswith('9') and len(K) == 16:
        print(f"#{i+1} {1}")
    else:
        print(f"#{i+1} {0}")