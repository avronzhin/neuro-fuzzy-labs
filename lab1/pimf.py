import numpy as np
import skfuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 5.05, 0.1)
mfx = skfuzzy.pimf(x, 2, 2.5, 3, 4.5)

plt.figure(figsize=(8, 5))
plt.plot(x, mfx)

plt.show()