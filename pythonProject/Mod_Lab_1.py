import random


def rando(x, x_len):
    x = x ** 2
    x_str = str(x)
    while ((2 * x_len) != len(x_str)):
        x_str = "0" + x_str
    x_str = x_str[:-(int(0.5 * x_len))]
    x_str = x_str[(int(0.5 * x_len)):]
    x = int(x_str)
    return (x)


def from_int_to_fraction(x):
    x_str = "0."+str(x)
    return x_str


a = random.randint(10 ** 31, 10 ** 32)
a = rando(a, 32)
c = from_int_to_fraction(a)
set_of_c = set()
while((c not in set_of_c) and (len(set_of_c)<20000)):
    set_of_c.add(c)
    a = rando(a, 32)
    c = from_int_to_fraction(a)
print(set_of_c)
print(len(set_of_c))