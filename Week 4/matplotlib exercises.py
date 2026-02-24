# Exercise 1 — Environment + first plot

import matplotlib.pyplot as plt
import numpy as np

y = [3, 7, 4, 9, 6]

fig, ax = plt.subplots()
ax.plot(y)
plt.show()