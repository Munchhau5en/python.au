import random
from numba import njit
import time


def func(x):
    return x ** 2


def Func(y):
    return y ** 3 / 3


@njit
def func_njit(x):
    return x ** 2


@njit
def Func_njit(y):
    return y ** 3 / 3


print("Введите левую границу интегрирования")
a = float(input())
print("Введите правую границу интегрирования")
b = float(input())
print("Введите количество точек (чем больше точек, тем выше точность)")
N = int(input())

start_time = time.time()
c = []
for i in range(N):
    c.append(random.uniform(a, b))

integral = float(0)
for j in range(N):
    integral += func(c[j])

leybnic = Func(b) - Func(a)

ans = integral * (b - a) / N

rel = min(ans / leybnic, leybnic / ans)

print("Интеграл вычисленный по методу Монте-Карло=", ans)
print("Интеграл вычисленный по формуле Ньютона-Лейбница=", leybnic)
print("Точность метода Монте-Карло в сравнении с реальным значением=", rel)
print("Время вычисления без ускорения:")
print("%s секунд" % (time.time() - start_time))

start_time_1 = time.time()
c = []
for i in range(N):
    c.append(random.uniform(a, b))

integral = float(0)
for j in range(N):
    integral += func_njit(c[j])

leybnic = Func_njit(b) - Func_njit(a)

ans = integral * (b - a) / N

rel = min(ans / leybnic, leybnic / ans)

print("Время вычисления с ускорением:")
print("%s секунд" % (time.time() - start_time_1))


'''

Введите левую границу интегрирования
-1
Введите правую границу интегрирования
1
Введите количество точек (чем больше точек, тем выше точность)
100000000
Интеграл вычисленный по методу Монте-Карло= 0.6666427383905213
Интеграл вычисленный по формуле Ньютона-Лейбница= 0.6666666666666666
Точность метода Монте-Карло в сравнении с реальным значением= 0.999964107585782
Время вычисления без ускорения:
103.41805624961853 секунд
Время вычисления с ускорением:
95.53132677078247 секунд

При меньшем кол-ве точек без njit работает чаще всего быстрее

'''
