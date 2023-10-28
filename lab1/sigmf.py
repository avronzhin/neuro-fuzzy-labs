import numpy as np
import skfuzzy
import matplotlib.pyplot as plt

x = np.arange(0, 5.05, 0.1)
mfx = skfuzzy.sigmf(x, 2,  3)

plt.figure(figsize=(8, 5))
plt.plot(x, mfx)

plt.show()