# 4406 모음이 보이지 않는 사람

T = int(input())
ls = ['a', 'e', 'i', 'o', 'u']
for i in range(T):
    string = list(input())
    a = []
    for j in string:
        if j not in ls:
            a.append(j)
    print(f"#{i+1} {''.join(a)}")