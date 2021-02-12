import numpy as np
import matplotlib.pyplot as plt
MAX = 10

for i in range(10):
    x = [k for k in range(MAX)]
    y = [j for j in range(i, i+MAX)]
    plt.plot(x, y)
    plt.pause(0.1)

# plt.plot([k for k in range(MAX)], [j for j in range(MAX)])
plt.show()
