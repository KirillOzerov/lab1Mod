import random
import numpy as np
import matplotlib.pyplot as plt


def rando(x, x_len):
    x = x ** 2
    x_str = str(x)
    while (2 * x_len) != len(x_str):
        x_str = "0" + x_str
    x_str = x_str[:-(int(0.5 * x_len))]
    x_str = x_str[(int(0.5 * x_len)):]
    x = int(x_str)
    return (x)


def from_int_to_fraction(x):
    x_str = str(x)
    while (18) != len(x_str):
        x_str = "0" + x_str
    x_str = "0." + x_str
    return float(x_str)


a = random.randint(0, 10**18)
print("Затравка:")
print(a)
print("Введите кол-во ожидаемых элементов в массиве:")
num = int(input())
a = rando(a, 18)
c = from_int_to_fraction(a)
set_of_c = []
while (c not in set_of_c) and (len(set_of_c) < num):
    set_of_c.append(c)
    a = rando(a, 18)
    c = from_int_to_fraction(a)
print(set_of_c)
print("Кол-во чисел в массиве:")
print(len(set_of_c))
# # расчет коэффициента Пирсона
# my_pirs = np.corrcoef(set_of_c)
# print("Коэфициент Пирсона:")
# print(my_pirs)
print("Кол-во разбиений = 20")
print("Ожмдаемое число попаданий на каждом участке:")
w = num/20
print(w)
a = 0
b = 0.05
pirs_coef = 0
num_of_c_in_each_diaposon = 0
for i in range(20):
    for c in set_of_c:
        if (c>=a) and (c<b):
            num_of_c_in_each_diaposon += 1
    pirs_coef += ((num_of_c_in_each_diaposon-w)**2)/w
    print("Участок номер: " + str(i+1))
    print("Кол-во попаданий:" + str(num_of_c_in_each_diaposon))
    num_of_c_in_each_diaposon = 0
    a += 0.05
    b += 0.05
print("Коэфициент Пирсона = " + str(pirs_coef))
plt.hist(set_of_c, bins=20, edgecolor="black")
plt.show()
# темыч момыч