# 2056 연월일 달력

T = int(input())

for T in range(1, T+1):
    number = input()
    yyyy = number[0:4]
    MM = number[4:6]
    DD = number[6:8]    
    if int(MM) > 12 or int(MM) < 1:
        print(f"#{T} -1")
    elif int(MM) == (1 or 3 or 5 or 7 or 8 or 10 or 12) and int(DD) > 31:
        print(f"#{T} -1")
    elif int(MM) == (4 or 6 or 9 or 11) and int(DD) > 30:
        print(f"#{T} -1")
    elif int(MM) == 2 and int(DD) > 28:
        print(f"#{T} -1")
    else:
        print(f"#{T} {yyyy}/{MM}/{DD}")