import numpy as np
import matplotlib.pyplot as plt
x = []
y = []
for i in range(1, 21):
    x.append(i)
for i in range(1, 21):
    y.append(i**3 + 6*i**2 + 3*i - 10)
plt.plot(x, y)
plt.show()