import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi * 2, np.pi * 2, 200)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, y)
plt.show()