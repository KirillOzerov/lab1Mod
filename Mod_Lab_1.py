import random
import numpy as np
import matplotlib.pyplot as plt


def rando(x, x_len):
    x_str = str(x ** 2)
    while (2 * x_len) != len(x_str):
        x_str = "0" + x_str
    x_str = x_str[(int(0.5 * x_len)):-(int(0.5 * x_len))]
    return int(x_str)


def from_int_to_fraction(x, x_len):
    x_str = str(x)
    while x_len != len(x_str):
        x_str = "0" + x_str
    x_str = "0." + x_str
    return float(x_str)


razor = 10
a = random.randint(0, 10 ** razor)
print("Затравка:")
print(a)
print("Введите кол-во ожидаемых элементов в массиве:")
num = int(input())
a = rando(a, razor)
c = from_int_to_fraction(a, razor)
set_of_c = []
while (c not in set_of_c) and (len(set_of_c) < num):
    set_of_c.append(c)
    a = rando(a, razor)
    c = from_int_to_fraction(a, razor)
print(set_of_c)
print(f'Первое повт: {set_of_c.index(c)}')
print("Период: " + str(len(set_of_c) - set_of_c.index(c)))
print("Кол-во чисел в массиве:")
print(len(set_of_c))
print("Введите кол-во разбиений:")
num_of_diaposon = int(input())
print("Ожмдаемое число попаданий на каждом участке:")
w = len(set_of_c) / num_of_diaposon
print(w)
a = 0
b = 1 / num_of_diaposon
pirs_coef = 0
num_of_c_in_each_diaposon = 0
for i in range(num_of_diaposon):
    for c in set_of_c:
        if (c > a) and (c < b):
            num_of_c_in_each_diaposon += 1
    pirs_coef += ((num_of_c_in_each_diaposon - w) ** 2) / w
    print("Участок номер: " + str(i + 1))
    print("Кол-во попаданий:" + str(num_of_c_in_each_diaposon))
    num_of_c_in_each_diaposon = 0
    a += 1 / num_of_diaposon
    b += 1 / num_of_diaposon
print("Коэфициент Пирсона = " + str(pirs_coef))

plt.hist(set_of_c, bins=num_of_diaposon, edgecolor="black")
plt.show()
