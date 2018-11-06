import codecademylib
from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1) #The top subplot is the first subplot from a grid with 2 rows and 1 column
plt.plot(x, straight_line)

plt.subplot(2, 2, 3) #The bottom left subplot is the third subplot from a grid with 2 rows and 2 columns
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace = 0.35, bottom = 0.2)
plt.show()