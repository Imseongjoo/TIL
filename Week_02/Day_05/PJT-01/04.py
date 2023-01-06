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