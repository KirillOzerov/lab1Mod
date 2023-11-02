import random
import matplotlib.pyplot as plt
import scipy
import math


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


def px1(x):
    return 0.0714285714 * x + 0.0714285714


def px2(x):
    return 0.2857142857


def px3(x):
    return 0.1428571428


def first_diaposon_fun(x):
    return -1 + (4 + 28 * x) ** 0.5


def second_diaposon_fun(x):
    return 1.5 + 3.5 * x


def third_diaposon_fun(x):
    return 7 * x - 1


def modification(x):
    if (x >= 0) and (x < 3/7):
        return first_diaposon_fun(x)
    if (x >= 3/7) and (x < 4/7):
        return second_diaposon_fun(x)
    if (x >= 4/7) and (x <= 1):
        return third_diaposon_fun(x)


razor = 10
# a = random.randint(0, 10 ** razor)
a = 8532978284
print("Затравка:")
print(a)
num = 99999999
a = rando(a, razor)
c = from_int_to_fraction(a, razor)
c = modification(c)
set_of_c = []
while (c not in set_of_c) and (len(set_of_c) < num):
    set_of_c.append(c)
    a = rando(a, razor)
    c = from_int_to_fraction(a, razor)
    c = modification(c)
print(set_of_c)
print(f'Первое повт: {set_of_c.index(c)}')
print("Период: " + str(len(set_of_c) - set_of_c.index(c)))
print("Длина апериодической части: " + str(set_of_c.index(c) - 1))
print("Кол-во чисел в массиве:")
print(len(set_of_c))
set_of_c = set_of_c[:set_of_c.index(c)]
print("Введите кол-во разбиений:")
# num_of_diaposon = int(input())
num_of_diaposon = 30
a = 1.0
b = a + 5 / num_of_diaposon
pirs_coef = 0
num_of_c_in_each_diaposon = 0
theory_num_of_c_in_diaposon = 0
for i in range(num_of_diaposon):
    for c in set_of_c:
        if (c > a) and (c < b):
            num_of_c_in_each_diaposon += 1
    if (a >= 1) and (a < 3):
        theory_num_of_c_in_diaposon = 0.5 * (px1(a) + px1(b)) * (b - a) * len(set_of_c)
    if (a >= 3) and (a < 4):
        theory_num_of_c_in_diaposon = px2(a) * (b - a) * len(set_of_c)
    if (a >= 4) and (a <= 6):
        theory_num_of_c_in_diaposon = px3(a) * (b - a) * len(set_of_c)
    pirs_coef += ((num_of_c_in_each_diaposon - theory_num_of_c_in_diaposon) ** 2) / theory_num_of_c_in_diaposon
    print("Участок номер: " + str(i + 1))
    print("Кол-во попаданий:" + str(num_of_c_in_each_diaposon))
    print("Кол-во попаданий:" + str(theory_num_of_c_in_diaposon))
    num_of_c_in_each_diaposon = 0
    a += 5 / num_of_diaposon
    b += 5 / num_of_diaposon
print("Коэфициент Пирсона = " + str(pirs_coef))
print(f'X**2: {scipy.stats.chi2.cdf(pirs_coef, df=(c - 1))}')
plt.hist(set_of_c, bins=num_of_diaposon, edgecolor="black")
plt.show()




















































































































