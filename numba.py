import random
from numba import njit


@njit
def func(x):
    return x**2


@njit
def Func(y):
    return y**3/3


print("Введите левую границу интегрирования")
a = float(input())
print("Введите правую границу интегрирования")
b = float(input())
print("Введите количество точек (чем больше точек, тем выше точность)")
N = int(input())
c = [0] * N
for i in range(N):
    c[i] = random.uniform(a, b)

integral = float(0)
for j in range(N):
    integral += func(c[j])

leybnic = Func(b) - Func(a)

ans = integral * (b - a) / N

rel = ans / leybnic

print("Интеграл вычисленный по методу Монте-Карло=", ans)
print("Интеграл вычисленный по формуле Ньютона-Лейбница=", leybnic)
print("Точность метода Монте-Карло в сравнении с реальным значением=", rel)