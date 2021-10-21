from methods import Euler, RungeKutta
from numpy import arange, exp
import matplotlib.pyplot as plt
H = 0.05
X0 = 0
Y0 = 0
XF = 1

def func(x, y):
    return x * exp(-(x**2)) - 2 * x * y

def funcY(x):
    return x**2 / (2 * exp(x**2))

euler = Euler(func, H)
# print(euler.calculate(X0, Y0, XF))
runge = RungeKutta(func, H)
# print(runge.calculate(X0, Y0, XF))
axisX = arange(X0, XF+H, H)
# print(axisX)
ys = []
for i in axisX:
    ys.append(funcY(i))
# print(ys)
plt.plot(axisX, euler.calculate(X0, Y0, XF))#Синяя, Метод Эйлера
plt.plot(axisX, runge.calculate(X0, Y0, XF))#Оранжевая, Метод Рунге-Кутта
plt.plot(axisX, ys, "--g")#Зеленая, обычная функция
plt.xlabel("H")
plt.ylabel("Y")
plt.show()

