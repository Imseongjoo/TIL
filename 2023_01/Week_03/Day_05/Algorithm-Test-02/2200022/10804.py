# 10804 문자열의 거울상

T = int(input())
for i in range(T):
    S = input()
    K = S[::-1]
    P = ''
    for j in K:
        if j == 'b':
            P += 'd'
        elif j == 'd':
            P += 'b'
        elif j == 'p':
            P += 'q'
        else:
            P += 'p'
    print(f"#{i+1} {P}")
