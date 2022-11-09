

import random
try:
    spisok = int(input("Enter size numbers: "))
    begin = -100
    end = 100
    my_num = list()
    for i in range(spisok):
        my_num.append(random.randint(begin, end))
    random.shuffle(my_num)
    print(my_num)
    my_num2 = list()
    for i in range(spisok):
        my_num2.append(random.randint(begin, end))
    random.shuffle(my_num2)
    print(my_num2)
    print()

    elsp = list()
    all = my_num + my_num2
    for i in all:
        elsp.append(i)
    print(elsp)
    all2 = list(set(my_num).symmetric_difference(set(my_num2)))
    print(all2)
    all3 = list(set(my_num).intersection(set(my_num2)))
    print(all3)
    all4 = list(set(all))
    print(all4)
    print(f"MAX = {max(all)} MIN = {min(all)}")
    
except Exception as e:
    print(e)