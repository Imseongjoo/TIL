with open('data/fruits.txt', 'r', encoding='UTF8') as file:
    count = 0
    for i in file:
        if len(i.strip('\n')):
            count += 1
    print(count)