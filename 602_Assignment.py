import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y vx x Plot")
plt.grid()
plt.show()