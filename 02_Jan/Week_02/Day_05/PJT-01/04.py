f = open('data/fruits.txt', 'r', encoding='UTF8')
text = f.read() 
string = text.split('\n')
dict_variable = {}
for char in string:
     if char in dict_variable.keys():
         dict_variable[char] += 1
     elif char not in dict_variable.keys():
         dict_variable[char] = 1

for key, value in dict_variable.items():
     print(key, value)

#      fruit_dict = {}

# with open('./data/fruits.txt', 'r') as f:
#     fruits = f.readlines()
#     for fruit in fruits:
#         fruit = fruit.strip()

#         if fruit not in fruit_dict:
#             fruit_dict[fruit] = 1

#         elif fruit in fruit_dict:
#             fruit_dict[fruit] += 1

# with open('./04.txt', 'w') as f:
#     for fruit, count in fruit_dict.items():
#         # print(fruit, count)
#         f.write(f'{fruit} {count} \n')