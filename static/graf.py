import matplotlib.pyplot as plt
import matplotlib.dates as mdates

with open(r'D:\Python\txt\hanasaki chile шум.txt', mode='r') as f:
    y = [float(i[:-2]) for i in f.readlines()]
fig, ax = plt.subplots()
x = [i for i in range(1, len(y) + 1)]
plt.plot(x, y)
ax.vlines(283, -75, 100,
          color='r',    #  цвет
          linewidth=1,    #  ширина
          linestyle=':')    #  начертание
ax.vlines(288, -75, 100,
          color='r',    #  цвет
          linewidth=1,    #  ширина
          linestyle=':')    #  начертание
plt.grid(which='major')
# plt.grid(which='minor', linestyle=':')
plt.minorticks_on()
plt.xlabel(r'$t, время$', fontsize=10)
plt.ylabel(r'$δ$', fontsize=16)
ax.axes.set_aspect(4.5)
plt.show()
