# 1. Input 대체
from collections import Counter
members = [
    "Jay", "John", "John", "Jay", "Jack", "Jack", "John", "Jo", "Jo", "Jack"
]

count = {}

for member in members:
    # if member in count:
    #     count[member] = count[member] + 1
    # else:
    #     count[member] = 1
    count[member] = count.get(member, 0) + 1

count_items = count.items()
print(count_items)

new_count_items = Counter(members)
print(new_count_items)


print(Counter('pen pineapple apple pen'))
print(Counter('pen pineapple apple pen').most_common())
print(Counter('pen pineapple apple pen').most_common(2))
