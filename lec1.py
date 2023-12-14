import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)

# task 1
sp = plt.subplot(321)
xA = [1, 10, 1000]
yA = []
for x_i in xA:
    a = 1 + x_i**2
    b = (np.e * (1 / (np.sin(x_i) + 1))) / (1.25 + (1 / x_i**1 * 5))
    y = np.log(b) / np.log(a)
    yA.append(y)
plt.scatter(xA, yA)
plt.title('Task 1')
plt.grid(True)

# task 2
sp = plt.subplot(322)
f2_x = x*x - x - 6
plt.plot(x, f2_x)
plt.title('Task 2')
plt.grid(True)

# task 3
sp = plt.subplot(323)
a = 1 + np.tan(1 / (1 + np.sin(x) ** 2))
b = (x**2 + 1) * np.exp(-1 * (abs(x) / 10))
f3_x = np.log(b) / np.log(a)
plt.plot(x, f3_x)
plt.title('Task 3')
plt.grid(True)

# task 4
sp = plt.subplot(324)
with plt.xkcd():
    f4_x = eval(input('Input formula fo task 4: '))
    plt.plot(x, f4_x)
    plt.title('Task 4')
    plt.grid(True)

# task 5
sp = plt.subplot(325)
xP = [1, 2, 3, 4, 5]
yP = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.scatter(xP, yP)
model1 = np.poly1d(np.polyfit(xP, yP, deg=1))
model2 = np.poly1d(np.polyfit(xP, yP, deg=2))
polyline = np.linspace(1, 5, 10)
plt.plot(polyline, model1(polyline), color='green')
plt.plot(polyline, model2(polyline), color='red')
plt.title('Task 5')
plt.grid(True)

# task 6
sp = plt.subplot(326)
def w_x(x_w):
    sum = 0
    for n in range(100):
        sum += 0.5 ** n * np.cos(3 ** n * np.pi * x_w)
    return sum
x_w = np.arange(-2, 2.01, 0.01)
plt.plot(x_w, w_x(x_w))
plt.title('Task 6')
plt.grid(True)

plt.show()

