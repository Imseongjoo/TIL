f = open('data/fruits.txt', 'r', encoding='UTF8')
text = f.read() 
list = set(text.split('\n'))
k = []
if 'berry' in list:
        k.append()
        print(len(k))
for i in list:
    if 'berry' in i:
        print(i)

# fruit_list = []
# fruit_count = 0

# with open('./data/fruits.txt', 'r') as f:
#     fruits = f.readlines()
#     for fruit in fruits:
#         fruit = fruit.strip()
#         if fruit[-5:] == 'berry':
#             if fruit not in fruit_list:
#                 fruit_list.append(fruit)
#                 fruit_count += 1

# with open('./03.txt', 'w') as f:
#     # print(fruit_count)
#     f.write(str(fruit_count) + '\n')

#     for fruit in fruit_list:
#         # print(fruit)
#         f.write(fruit + '\n')      