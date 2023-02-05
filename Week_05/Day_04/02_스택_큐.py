numbers = [10, 2, 5, 7]

for number in numbers: 
    if number % 2 == 0:
        numbers.pop()
    print(number)

# 1. number 10 => pop => [10, 2, 5]
# 2. number 2 => pop => [10, 2]

# (1) 
# 별도의 리스트에 추가를 하거나, 관리를 하는 형태
# (2)
# 인덱스로 접근해서 값을 변화시켜..
# (3)
# 리스트를 copy해서 쓴다. 

a = 'apple'

# 파이썬
# a.startswith('a')

# 'a'로 시작하는지를 알고 싶음
# a[0] == 'a' 

# 'ap'로 시작하는지를 알고 싶음
# a[:2] == 'ap' 

# 길이가 N인 문자로 시작하는지 알고 싶음 

# Input
N = 7

# queue = [i for i in range(1, N+1)]
queue = list(range(1, N+1))
discard_cards = []
# 1장 남을때까지 반복 => while
while len(queue) > 1:
    # 우선, 제일 위에 있는 카드를 바닥에 버린다. 
    # queue에서 제일 위 : pop(0)
    discard_cards.append(queue.pop(0))
    #  그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    queue.append(queue.pop(0))
    print(discard_cards, queue)

# 1 3 5 7 4 2 6
print(*discard_cards, queue[0])

# 0이 나오면 가장 최근에 쓴 수를 지운다. 
 
# Input 
numbers = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6] 

stack = []
# 로직(순회)
for number in numbers:
    # 0이면 스택에서 꺼내버리고
    if number == 0:
        stack.pop()
    # 아니면 스택에 추가한다. 
    else:
        stack.append(number)

print(sum(stack))