

try:
    import random

    size = int(input(" Enter amount numbers: "))
    begin = -100
    end = 100
    my_text = []

    for l in range(size):
        my_text.append(random.randint(begin, end))

    random.shuffle(my_text)
    videmni_num = []
    plus_num = []
    parni_num = []
    neparni_num = []

    mul = 1
    mul2 = 1
    mul3 = []

    print(my_text)
    for g in my_text:
        if g < 0:
            videmni_num.append(g)

        if g % 2 == 0:
            parni_num.append(g)

        if g % 3 == 0:
            neparni_num.append(g)
    print()
    print("====Добуток елементів з індексами кратними 3==== ")
    for m in range(0, len(my_text), 3):
        print(f"{mul} * {my_text[m]}[{m}] = ", end=" ")
        mul *= my_text[m]
        print(mul)
    print("=================================================")
    print()
    print("======Числа між мінімальним та максимальним елементом======")
    start = my_text.index(min(my_text))
    end = my_text.index(max(my_text))
    if start > end:
        start, end = end, start

    print(f"min = {my_text[start]} max = {my_text[end]}")

    for i in range(start, end + 1):
        print(f"{mul2} * {my_text[i]}[{i}]", end=" ")
        mul2 *= my_text[i]
        print(f"Результат = {mul2}")

    print("==========================================================")

    print(f"Сумма відємних чисел = {sum(videmni_num)}")
    print(f"Сумма парних чисел = {sum(parni_num)}")
    print(f"Сумма непарних чисел = {sum(neparni_num)}")

    for c in my_text:
        if c > 0:
            plus_num.append(c)  # плюсові числа
    print(f"Сума елементів між першим та останнім додатнім значенням: {sum(plus_num[1:-1])}")

except Exception as ex:
    print(ex)