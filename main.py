# Removing the Top and Right axis (spines) in Matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 150)
y = np.sin(x)

ax = plt.subplot(111)
ax.plot(x, y)

# 👇️ remove the top and right axis
ax.spines[['right', 'top']].set_visible(False)

plt.show()