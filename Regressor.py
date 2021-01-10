import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import linregress



def dataset():
    mx = 0
    n = int(input("введите количество точек:  "))
    x = np.empty(n)
    y = np.empty(n)
    xe, ye, ye1 = [], [], []
    print("введите координаты точек:")
    for i in range(0, n):
        x[i] = float(input())
        if i == 0:
            mx = x[i]
            nx = x[i]
        if x[i] > mx:
            mx = x[i]
        if x[i] < nx:
            nx = x[i]
        y[i] = float(input())
        if y[i] > 0:
            ye.append(math.log(y[i]))
            xe.append(x[i])
            ye1.append(y[i])
    xe = np.array(xe)
    ye = np.array(ye)
    ye1 = np.array(ye1)
    return x, y, nx, mx, xe, ye, ye1

x, y, nx, mx, xe, ye, ye1 = dataset()


def fufu(p, x, y):
    d = 0
    q = 0
    for i in range(len(x)):
        for j in range(len(p)):
            q = q + p[j] * x[i]**(len(p) - j)
        d = d + (y[i] - q) ** 2
        q = 0
    return d





slope, intercept, r_value, p_value, std_err = linregress(x, y)
grx = [0, int(mx) + 3]
gr = [intercept, mx*slope+intercept]
plt.subplot(131)
plt.scatter(x, y)
plt.plot(grx, gr,color='k')
#plt.subplot(132)
#plt.scatter(names, values)
    #print(slope,intercept,r_value,p_value,std_err)


reg = np.polyfit(xe, ye, 1)
xe2 = np.arange(0, int(mx + 4), 1)
ye2 = np.zeros(int(mx + 4))
for i in range(len(xe2)):
    ye2[i] = math.exp(reg[0]*xe2[i] + reg[1])
plt.subplot(132)
plt.plot(xe2, ye2, color='k')
plt.scatter(xe, ye1)


p4 = np.polyfit(x, y, 4)
p3 = np.polyfit(x, y, 3)
p2 = np.polyfit(x, y, 2)

x2 = np.arange(0, int(mx + 4), 1)

y2 = np.zeros(int(mx + 4))
y3 = np.zeros(int(mx + 4))
y4 = np.zeros(int(mx + 4))
for i in range(len(x2)):
    y4[i] = p4[0] * x2[i] ** 4 + p4[1] * x2[i] ** 3 + p4[2] * x2[i] ** 2 + p4[3] * x2[i] ** 1 + p4[4]
    y3[i] = p3[0] * x2[i] ** 3 + p3[1] * x2[i] ** 2 + p3[2] * x2[i] ** 1 + p3[3]
    y2[i] = p2[0] * x2[i] ** 2 + p2[1] * x2[i] ** 1 + p2[2]
plt.subplot(133)

plt.plot(x2, y2, color='b')
plt.plot(x2, y3, color='g')
plt.plot(x2, y4, color='r')
plt.scatter(x, y)
plt.show()
