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
for a in range(9959943278, 10000000000):
    num = 1100000000
    zat = a
    a = rando(a, razor)
    c = from_int_to_fraction(a, razor)
    set_of_c = []
    while (c not in set_of_c) and (len(set_of_c) < num):
        set_of_c.append(c)
        a = rando(a, razor)
        c = from_int_to_fraction(a, razor)
    if len(set_of_c) - set_of_c.index(c) > 10000:
        print(set_of_c)
        print("Затравка:")
        print(zat)
        print(f'Первое повт: {set_of_c.index(c)}')
        print("Период: " + str(len(set_of_c) - set_of_c.index(c)))
        print("Кол-во чисел в массиве:")
        print(len(set_of_c))