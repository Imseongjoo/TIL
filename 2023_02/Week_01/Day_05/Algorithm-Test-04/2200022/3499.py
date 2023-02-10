# 3499 퍼펙트 셔플

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(str, input().split()))

    if len(cards)%2 == 1:
        new_arr1 = cards[0:len(cards)//2+1]
        new_arr2 = cards[len(cards)//2+1:]
    else:
        new_arr1 = cards[0:len(cards)//2]
        new_arr2 = cards[len(cards)//2:]

    new_cards = []
    for i in range(N):
        if i%2 == 0:
            new_cards.append(new_arr1.pop(0))
        elif i%2 == 1:
            new_cards.append(new_arr2.pop(0))

    print('#{}'.format(tc), end=' ')
    print(*new_cards)