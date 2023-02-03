# 1983 조교의 성적 매기기

T = int(input())
grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
for _ in range(T):
    N, K = map(int, input().split())
    ls = []
    for i in range(N):
        a, b, c = map(int, input().split())
        score = a*0.35 + b*0.45 + c*0.2
        ls.append((score, i+1))
    ls.sort()
    for j in range(N):
        if ls[j][1] == K:
            print(f"#{_+1} {grade[(j//(N//10))%10]}")