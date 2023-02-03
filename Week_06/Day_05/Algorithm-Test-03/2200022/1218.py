# 1218 [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

for i in range(10):
    T = int(input())
    string = list(map(str, input()))
    ls = []
    left = ["(", "{", "[", "<"]
    right = [")", "}", "]", ">"]
    for j in range(T):
        if string[j] in left:
            ls.append(string[j])
        if string[j] in right:
            if right.index(string[j]) == left.index(ls[-1]):
                ls.pop()   
            else:
                break     
    ans = 0
    if len(ls) == 0:
        ans = 1
    print(f"#{i+1} {ans}")