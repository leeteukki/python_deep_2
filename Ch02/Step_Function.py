#utf -8

import numpy as np
import matplotlib.pylab as plt

def Step_function(x):
    return np.array (x > 0, dtype = np.int)

x = np.arange(-0.5, 0.5, 0.1)
y = Step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()