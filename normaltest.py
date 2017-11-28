import numpy as np
import matplotlib.pyplot as plt

y = np.random.normal(size=(100))
plt.close('all')
plt.stem(y)
plt.show()

