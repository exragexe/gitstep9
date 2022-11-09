

import random
try:
    spisok = int(input("Enter size numbers: "))
    begin = -100
    end = 100
    my_num = []
    for i in range(spisok):
        my_num.append(random.randint(begin, end))
    random.shuffle(my_num)
    print(my_num)

    num1 = list()
    num2 = list()
    num3 = list()
    num4 = list()

    for i in my_num:
        if i % 2 ==0:
            num1.append(i)
        if i % 3 == 0:
            num2.append(i)
        if i < 0:
            num3.append(i)
        if i >= 0:
            num4.append(i)
    print(f"Парні числа - {num1}")
    print(f"Не парні числа - {num2}")
    print(f"Від'ємні числа - {num3}")
    print(f"Додатні числа - {num4}")

except Exception as e:
    print(e)
